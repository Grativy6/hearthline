"""Prepare, or explicitly run, the bounded CPX formal checks. No implicit Lean run."""
from pathlib import Path
import argparse
import datetime as dt
import hashlib
import json
import os
import re
import subprocess
import time

ROOT = Path(__file__).resolve().parent
MODULES = ["CPX.Capsule", "CPX.ProtectedReturn", "CPX.Information",
           "CPX.Diagnostics", "CPX.Resolution", "CPX"]
TOOLCHAIN = "leanprover/lean4:v4.32.1"
ALLOWED_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path, value):
    path = Path(path)
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    os.replace(temp, path)


def lean_code(text):
    """Remove the nested comments used in these files before the static token scan."""
    out, i, depth = [], 0, 0
    while i < len(text):
        if text.startswith("/-", i):
            depth += 1
            i += 2
        elif depth and text.startswith("-/", i):
            depth -= 1
            i += 2
        elif depth:
            if text[i] == "\n":
                out.append("\n")
            i += 1
        elif text.startswith("--", i):
            i = text.find("\n", i)
            if i == -1:
                break
        else:
            out.append(text[i])
            i += 1
    if depth:
        raise ValueError("Unclosed Lean block comment")
    return "".join(out)


def source_files():
    return sorted([*ROOT.glob("*.lean"), *ROOT.joinpath("CPX").glob("*.lean"),
                   ROOT / "THEOREMS.json", ROOT / "lakefile.toml",
                   ROOT / "lake-manifest.json", ROOT / "lean-toolchain", Path(__file__)])


def preparation(args):
    if (ROOT / "lean-toolchain").read_text().strip() != TOOLCHAIN:
        raise ValueError("CPX toolchain pin changed")
    dep = args.dependency_project.resolve()
    if (dep / "lean-toolchain").read_text().strip() != TOOLCHAIN:
        raise ValueError("Dependency project uses a different toolchain")
    pins = read_json(ROOT / "lake-manifest.json")
    supplied = read_json(dep / "lake-manifest.json")
    wanted = {p["name"]: p["rev"] for p in pins["packages"]}
    actual = {p["name"]: p["rev"] for p in supplied["packages"]}
    if wanted != actual:
        raise ValueError("Dependency revisions differ")
    suffix = ".exe" if os.name == "nt" else ""
    binaries = {n: args.toolchain_dir.resolve() / "bin" / (n + suffix)
                for n in ("lean", "leanchecker")}
    if not all(p.is_file() for p in binaries.values()):
        raise ValueError("Pinned Lean and kernel checker must already be installed")
    registry = read_json(ROOT / "THEOREMS.json")
    names = [row["name"] for row in registry["declarations"]]
    if len(names) != len(set(names)):
        raise ValueError("Duplicate registered theorem")
    declared, imports = [], set()
    for module in MODULES:
        path = ROOT / (module.replace(".", "/") + ".lean")
        code = lean_code(path.read_text(encoding="utf-8"))
        if re.search(r"\b(sorry|admit|axiom|native_decide|unsafe|implemented_by|run_tac)\b", code):
            raise ValueError("Proof hole or unapproved escape in " + module)
        ns = re.findall(r"^namespace\s+(\S+)", code, re.M)
        if module != "CPX" and ns != [module]:
            raise ValueError("Unexpected namespace layout: " + module)
        declared.extend(module + "." + n for n in re.findall(r"^theorem\s+(\w+)", code, re.M))
        imports.update(re.findall(r"^import\s+(\S+)", code, re.M))
    if set(declared) != set(names):
        raise ValueError("Theorem registry does not match candidate declarations")
    inspector = (ROOT / "Inspect.lean").read_text(encoding="utf-8")
    if re.findall(r"^#print axioms (\S+)$", inspector, re.M) != names:
        raise ValueError("Axiom inspection is incomplete")
    if re.findall(r"^#check (\S+)$", inspector, re.M) != names:
        raise ValueError("Statement inspection is incomplete")
    mathlib = dep / ".lake/packages/mathlib"
    for module in imports:
        if module.startswith("CPX"):
            continue
        relative = Path(module.replace(".", "/"))
        if not (mathlib / relative.with_suffix(".lean")).is_file():
            raise ValueError("Missing direct import source: " + module)
        if not (mathlib / ".lake/build/lib/lean" / relative.with_suffix(".olean")).is_file():
            raise ValueError("Missing direct import cache: " + module)
    lock = read_json(args.source_lock)
    sources = []
    for item in lock["inputs"]:
        path = (args.source_lock.parent / item["path"]).resolve()
        if sha(path) != item["sha256"]:
            raise ValueError("Controlling source changed: " + item["role"])
        sources.append({"role": item["role"], "sha256": item["sha256"]})
    libs = [dep / ".lake/packages" / n / ".lake/build/lib/lean" for n in wanted]
    libs = [p for p in libs if p.is_dir()]
    return {"status": "PREPARED_NOT_RUN", "lean_processes_started": 0,
            "claim_families": 4, "named_theorems": len(names), "sources": sources,
            "candidate_sha256": {p.relative_to(ROOT).as_posix(): sha(p) for p in source_files()},
            "toolchain": TOOLCHAIN, "dependency_revisions": wanted,
            "tool_sha256": {n: sha(p) for n, p in binaries.items()},
            "direct_imports": sorted(imports),
            "limits": "Static checks only; candidate proofs are uncompiled."}, binaries, libs, names


def run(args):
    receipt, binaries, libs, names = preparation(args)
    if not args.run:
        if args.output:
            args.output.mkdir(parents=True, exist_ok=False)
            write_json(args.output / "preparation.json", receipt)
        print(json.dumps(receipt, indent=2))
        return
    if args.output is None:
        raise ValueError("Execution requires a fresh --output directory")
    out = args.output.resolve()
    out.mkdir(parents=True, exist_ok=False)
    build = out / "build/lib/lean"
    build.mkdir(parents=True)
    env = os.environ.copy()
    env["LEAN_PATH"] = os.pathsep.join(map(str, [build, *libs]))
    env.pop("LEAN_SRC_PATH", None)
    env.pop("LEAN_SYSROOT", None)
    receipt.update(status="IN_PROGRESS", commands=[], utc=dt.datetime.now(dt.timezone.utc).isoformat(),
                   assurance="Pinned Lean kernel replay; cached imports trusted; no independent kernel or full library audit.")
    deadline = time.monotonic() + 1800
    original = receipt["candidate_sha256"]
    receipt_path = out / "receipt.json"
    write_json(receipt_path, receipt)

    def command(label, argv):
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise TimeoutError("Attempt elapsed ceiling reached")
        started = time.monotonic()
        stdout_path, stderr_path = out / (label + ".stdout.txt"), out / (label + ".stderr.txt")
        row = {"label": label, "argv": list(map(str, argv)), "status": "RUNNING"}
        receipt["commands"].append(row)
        receipt["lean_processes_started"] += 1
        write_json(receipt_path, receipt)
        print("START " + label, flush=True)
        try:
            with stdout_path.open("wb") as stdout, stderr_path.open("wb") as stderr:
                completed = subprocess.run(row["argv"], cwd=ROOT, env=env, stdout=stdout,
                                           stderr=stderr, timeout=min(300, remaining), check=False)
            row.update(status="EXITED", exit_code=completed.returncode)
        except subprocess.TimeoutExpired:
            row.update(status="TIMEOUT", exit_code=None)
            raise
        finally:
            row.update(seconds=time.monotonic() - started,
                       stdout_sha256=sha(stdout_path), stderr_sha256=sha(stderr_path))
            write_json(receipt_path, receipt)
        if completed.returncode:
            raise RuntimeError(label + " failed; retain its full output")
        return stdout_path.read_text(encoding="utf-8", errors="replace")

    try:
        version = command("lean-version", [binaries["lean"], "--version"])
        if not re.search(r"\bversion 4\.32\.1\b", version):
            raise ValueError("Actual Lean version differs")
        for module in MODULES:
            relative = Path(module.replace(".", "/"))
            target = build / relative.with_suffix(".olean")
            target.parent.mkdir(parents=True, exist_ok=True)
            command("compile-" + module, [binaries["lean"], "-R", ROOT, "-j", "1", "-M", "4096",
                    "-o", target, relative.with_suffix(".lean")])
        text = command("statements-and-axioms", [binaries["lean"], "-R", ROOT, "-M", "4096", "Inspect.lean"])
        rows = re.findall(r"'([^']+)' (?:does not depend on any axioms|depends on axioms:\s*\[(.*?)\])", text, re.S)
        raw_axioms = {n: sorted(a.strip() for a in raw.split(",") if a.strip()) for n, raw in rows}
        # pp.universes prints e.g. Classical.choice.{u}; preserve that output and
        # compare the declaration name, not its universe instantiation.
        axioms = {n: sorted(re.sub(r"\.\{[^{}]*\}$", "", a) for a in values)
                  for n, values in raw_axioms.items()}
        if len(rows) != len(names) or set(axioms) != set(names):
            raise ValueError("Missing or duplicate axiom output")
        if any(set(values) - ALLOWED_AXIOMS for values in axioms.values()):
            raise ValueError("Unexpected axiom dependency")
        receipt["axioms"] = axioms
        receipt["raw_axioms"] = raw_axioms
        for module in MODULES[:-1]:
            output = command("kernel-" + module, [binaries["leanchecker"], "--verbose", module])
            if not re.search(r"^replaying " + re.escape(module) + r"$", output, re.M):
                raise ValueError("Kernel replay target not witnessed: " + module)
        refreshed, _, _, _ = preparation(args)
        if original != refreshed["candidate_sha256"] or receipt["tool_sha256"] != refreshed["tool_sha256"]:
            raise ValueError("Candidate or tool changed during the run")
        receipt.update(status="PASS_FORMAL_CHECKS_REQUIRES_SOURCE_REVIEW",
                       source_to_formal_review="OPEN_MANUAL", candidate_unchanged=True)
    except Exception as error:
        receipt.update(status="FAILED_OR_INCOMPLETE", error=type(error).__name__ + ": " + str(error))
        raise
    finally:
        receipt["finished_utc"] = dt.datetime.now(dt.timezone.utc).isoformat()
        write_json(receipt_path, receipt)
    print(receipt["status"], flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dependency-project", type=Path, required=True)
    parser.add_argument("--toolchain-dir", type=Path, required=True)
    parser.add_argument("--source-lock", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--run", action="store_true", help="Start Lean only after the execution key is turned")
    run(parser.parse_args())
