# Verify the public lab

Use Python 3.11 or 3.12 and a Git clone of the public repository. The structural
checks resolve retired sources from one pinned public commit, without a
private Cabin checkout or credentials. Fetch that public evidence if it is not
already present, then run the checks from the repository root:

```sh
git fetch --no-tags --depth=1 origin f5c69b912761f29e2c82f83d1fe412fc83ec873a
python -B tools/check_public_lab.py
python -B tools/check_branch_archive.py
python -B tools/check_change_history.py
python -B tools/check_research_station.py
python -B tools/check_return_queue.py
python -B tools/check_tether.py
```

The first command needs network access. With the pinned Git objects present,
the checks need no model calls. `check_public_lab.py` checks the split map,
original source hashes, unchanged full history records, unchanged CPX package
and current Markdown links. A missing current link fails; only the explicitly
frozen historical records may resolve retired links through the original tree.
The other checkers retain their structural, source-binding and authority-limit
assertions. Structural passes do not demonstrate a deployed system or prove
the natural-language contracts.

For the implemented toolkit, follow the [installation instructions](TOOLKIT_RUNTIME.md),
install `pytest==8.4.2`, and run `python -m pytest -q tests`. The toolkit CI also
installs the public SeedPEA adapter at its pinned revision and runs its real
cross-adapter equivalence test on Windows/Linux with Python 3.11/3.12.

The [CPX companion](../research/context-parallax/lean/README.md) has its own
source locks, replay instructions and assurance limits. This organization pass
compares its exact bytes; it does not rerun Lean or expand formal coverage.
