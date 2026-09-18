"""Bounded, source-attributed science and mathematics helpers.

These are ordinary software checks.  They do not infer a unique cause, prove a
Hodge conjecture, or claim neural/model performance.  Every operation returns
JSON-compatible data and an explicit ``effects: []`` marker.
"""
from __future__ import annotations

from decimal import Decimal, InvalidOperation, localcontext
from fractions import Fraction
from math import gcd, isfinite
import hashlib
import json
import re
from typing import Any, Callable

MAX_ITEMS = 256
MAX_INT = 10**12

# Stable public/source-inventory identities. These are references, not copied
# source text and not claims of conformance.
SOURCE_REFERENCES = {
    "GOLD": {"id": "MATH-GOLD-0.1", "version": "0.1", "public_reference": "https://zenodo.org/records/22236848", "locator": "Sections 4-7, 9"},
    "GPPR": {"id": "MATH-GPPR-0.1", "version": "0.1", "public_reference": "https://zenodo.org/records/22225414", "locator": "Sections 5-8"},
    "BRIDGE": {"id": "SOFT-BRIDGE-0.4", "version": "0.4", "public_reference": "https://zenodo.org/records/22699551", "locator": "Instance Record; Detection Binding; Four Sector Endpoint; Minimal Repair"},
    "APCI": {"id": "MATH-APCI-1.0.0", "version": "1.0.0", "locator": "Declared Interface; protected-query collision"},
    "A0BK": {"id": "SOFT-A0BK-0.10.0", "version": "0.10.0", "locator": "receipt/account grammar and residual lineage"},
    "FBT": {"id": "SOFT-FBT-0.1", "version": "0.1", "locator": "TRACE_ONLY, SHADOW, GOVERNING distinctions"},
}


def _out(status: str, **values: Any) -> dict[str, Any]:
    return {"status": status, "effects": [], **values}


def _source(payload: dict[str, Any]) -> dict[str, Any]:
    return {"source": payload.get("source", "unspecified"),
            "locator": payload.get("locator"), "version": payload.get("version")}


def observation_contract(payload: dict[str, Any]) -> dict[str, Any]:
    """Check that an observation separates observation, interpretation, and simulation."""
    if not isinstance(payload, dict):
        return _out("INVALID", reason="payload must be an object")
    required = ("question", "raw", "baseline", "method", "aperture", "calibration", "uncertainty")
    missing_fields = [key for key in required if key not in payload]
    channels = payload.get("channels", [])
    if not isinstance(channels, list) or len(channels) > MAX_ITEMS:
        return _out("INVALID", reason="channels must be a bounded list")
    names = [str(x.get("name", "")) for x in channels if isinstance(x, dict)]
    typed_channels = all(isinstance(x, dict) and x.get("kind") in {"observed", "interpretation", "simulation"} for x in channels)
    missing = [n for n in ("observation", "interpretation") if n not in names]
    if payload.get("simulation") is True and "simulation" not in names:
        missing.append("simulation")
    if missing_fields:
        return _out("INCOMPLETE", missing_fields=missing_fields, missing_channels=missing,
                    valid=False, attribution=_source(payload))
    valid = isinstance(payload.get("question"), str) and bool(payload.get("question")) and payload.get("raw") is not None and payload.get("baseline") is not None and isinstance(payload.get("method"), str) and payload.get("aperture") is not None and payload.get("calibration") is not None and payload.get("uncertainty") is not None and typed_channels and bool(payload.get("valid", True))
    return _out("DECLARED_CONTRACT_CHECKED" if not missing and valid else "INCOMPLETE", missing_fields=[], missing_channels=missing,
                valid=valid, typed_channels=typed_channels,
                channels=names, observation=payload.get("observation"),
                interpretation=payload.get("interpretation"),
                simulation=payload.get("simulation"), attribution=_source(payload))


def compare_prerequisites(payload: dict[str, Any]) -> dict[str, Any]:
    """Compare two finite prerequisite sets without deciding why they differ."""
    a, b = payload.get("baseline", []), payload.get("comparison", [])
    if not all(isinstance(x, list) and len(x) <= MAX_ITEMS for x in (a, b)):
        return _out("INVALID", reason="baseline and comparison must be bounded lists")
    sa, sb = {str(x) for x in a}, {str(x) for x in b}
    method_a, method_b = payload.get("method_baseline"), payload.get("method_comparison")
    aperture_a, aperture_b = payload.get("aperture_baseline"), payload.get("aperture_comparison")
    changed = bool(sa-sb or sb-sa or method_a != method_b or aperture_a != aperture_b)
    return _out("PASS", added=sorted(sb-sa), removed=sorted(sa-sb), common=sorted(sa&sb),
                changed=changed, comparator_changed=method_a != method_b or aperture_a != aperture_b,
                attribution=_source(payload))


def detection_limit(payload: dict[str, Any]) -> dict[str, Any]:
    """Return a declared detection-limit comparison; no causal inference."""
    try:
        value, limit = Decimal(str(payload["value"])), Decimal(str(payload["limit"]))
        if not value.is_finite() or not limit.is_finite() or limit < 0:
            raise InvalidOperation
    except (KeyError, InvalidOperation, ValueError):
        return _out("INVALID", reason="finite value and non-negative limit required")
    return _out("DETECTED" if value >= limit else "BELOW_LIMIT", value=str(value),
                limit=str(limit), relation="at_or_above_limit" if value >= limit else "below_limit",
                attribution=_source(payload))


def simulation_vs_observation(payload: dict[str, Any]) -> dict[str, Any]:
    """Classify declared data as observed, simulated, or mixed."""
    kind = payload.get("kind")
    if kind not in {"observation", "simulation", "mixed"}:
        return _out("INVALID", reason="kind must be observation, simulation, or mixed")
    return _out("PASS", kind=kind, interpretation=payload.get("interpretation"),
                supports_causal_claim=False, attribution=_source(payload))


def residual_alternatives(payload: dict[str, Any]) -> dict[str, Any]:
    """Preserve unresolved alternatives and identify missing discriminators."""
    alternatives = payload.get("alternatives", [])
    if not isinstance(alternatives, list) or len(alternatives) > MAX_ITEMS:
        return _out("INVALID", reason="alternatives must be bounded list")
    missing = payload.get("missing_discriminators", [])
    if not isinstance(missing, list) or len(missing) > MAX_ITEMS:
        return _out("INVALID", reason="missing_discriminators must be bounded list")
    return _out("RESIDUAL" if alternatives else "NONE", alternatives=alternatives,
                missing_discriminators=missing, unique_cause=False, attribution=_source(payload))


def finite_endpoint(payload: dict[str, Any]) -> dict[str, Any]:
    """Validate a finite endpoint/readout while retaining a side trace."""
    point = payload.get("point")
    if not isinstance(point, list) or not point or len(point) > MAX_ITEMS:
        return _out("INVALID", reason="point must be a non-empty bounded list")
    try:
        vals = [_bounded_fraction(x) for x in point]
    except (InvalidOperation, ValueError):
        return _out("INVALID", reason="endpoint coordinates must be finite")
    return _out("PASS", endpoint=[str(v.numerator) if v.denominator == 1 else f"{v.numerator}/{v.denominator}" for v in vals], exact=True, readout=payload.get("readout"),
                side_trace=payload.get("side_trace", []), attribution=_source(payload))


def readout_binding(payload: dict[str, Any]) -> dict[str, Any]:
    """Bind a readout to an endpoint without replacing the endpoint."""
    if "endpoint_id" not in payload or "readout" not in payload:
        return _out("INCOMPLETE", missing=[x for x in ("endpoint_id", "readout") if x not in payload])
    return _out("BOUND", endpoint_id=str(payload["endpoint_id"]), readout=payload["readout"],
                endpoint_unchanged=True, attribution=_source(payload))


def side_trace_repair(payload: dict[str, Any]) -> dict[str, Any]:
    """Repair a missing side trace only when its explicit predecessor is supplied."""
    trace, predecessor = payload.get("trace"), payload.get("predecessor")
    if not isinstance(trace, list) or len(trace) > MAX_ITEMS:
        return _out("INVALID", reason="trace must be a bounded list")
    if predecessor is None:
        return _out("INSUFFICIENT", reason="explicit predecessor required", residual=True)
    return _out("REPAIRED", trace=[predecessor, *trace], answer_recovered=False,
                full_object_recovered=False, attribution=_source(payload))


def apci_cost(payload: dict[str, Any]) -> dict[str, Any]:
    """Check a finite protected-query collision witness; no scalar cost."""
    required = ("protected_question", "retained_a", "retained_b", "answer_a", "answer_b")
    missing = [key for key in required if key not in payload]
    if missing:
        return _out("INSUFFICIENT_EVIDENCE", missing=missing, scalar_cost=None, attribution=_source(payload))
    protected = payload.get("protected_question")
    retained_a, retained_b = payload.get("retained_a"), payload.get("retained_b")
    answer_a, answer_b = payload.get("answer_a"), payload.get("answer_b")
    if retained_a == retained_b and answer_a != answer_b:
        return _out("COLLISION", protected_question=protected, packet_equal=True,
                    answers_differ=True, scalar_cost=None, side_trace_required=True,
                    attribution=_source(payload))
    return _out("NO_WITNESS_NOT_SUFFICIENT", protected_question=protected, packet_equal=retained_a == retained_b,
                answers_differ=answer_a != answer_b, scalar_cost=None, attribution=_source(payload))


def bridge_repair(payload: dict[str, Any]) -> dict[str, Any]:
    """Check finite source/readout fibers and protected-answer repair."""
    required = ("source_map", "readout_map", "side_trace_map", "protected_query")
    missing = [x for x in required if x not in payload]
    if missing:
        return _out("INCOMPLETE", missing=missing, residual=True)
    source_map, readout_map, side_map = payload["source_map"], payload["readout_map"], payload["side_trace_map"]
    if not isinstance(source_map, dict) or not isinstance(readout_map, dict) or not isinstance(side_map, dict):
        return _out("INVALID", reason="source_map and readout_map must be objects")
    fibers: dict[str, list[str]] = {}
    for source in source_map:
        if str(source) not in readout_map or str(source) not in side_map:
            return _out("INCOMPLETE", reason="side_trace/readout missing for source point", source=str(source))
        key = json.dumps([readout_map[str(source)], side_map[str(source)]], sort_keys=True, separators=(",", ":"))
        fibers.setdefault(key, []).append(str(source))
    query = payload["protected_query"]
    answers = {str(k): source_map.get(str(k)) for k in query} if isinstance(query, list) else {}
    if not isinstance(query, list) or not query or any(str(k) not in source_map for k in query):
        return _out("INVALID", reason="protected_query must name existing source points")
    fiber_answers = []
    for members in fibers.values():
        if any(not isinstance(source_map[m], dict) or "protected_answer" not in source_map[m] for m in members):
            return _out("INCOMPLETE", reason="protected_answer missing from source point", fibers=fibers)
        vals = {json.dumps(source_map[m].get("protected_answer"), sort_keys=True) for m in members}
        fiber_answers.append({"members": members, "answer_constant": len(vals) == 1, "answers": sorted(vals)})
    sufficient = all(x["answer_constant"] for x in fiber_answers)
    full = bool(payload.get("domain_complete", False)) and all(len(x["members"]) == 1 for x in fiber_answers)
    return _out("PASS" if sufficient else "INSUFFICIENT", source_count=len(source_map), readout_fibers=fibers,
                protected_answers=answers, fibers=fiber_answers, answer_recovered=sufficient,
                full_object_recovered=full, residual=None if sufficient else "protected answer varies within fiber",
                attribution=_source(payload))


def _numbers(payload: dict[str, Any], key: str, width: int | None = None) -> list[Fraction] | None:
    values = payload.get(key)
    if not isinstance(values, list) or len(values) > MAX_ITEMS or (width and len(values) != width):
        return None
    try:
        out = [_bounded_fraction(v) for v in values]
    except (ValueError, ZeroDivisionError):
        return None
    if any(abs(v.numerator) > MAX_INT or v.denominator > MAX_INT for v in out):
        return None
    return out


def _bounded_fraction(value: Any) -> Fraction:
    text = str(value)
    if len(text) > 128:
        raise ValueError("numeric token too long")
    match = re.search(r"[eE]([+-]?\d+)$", text)
    if match and abs(int(match.group(1))) > 10000:
        raise ValueError("exponent too large")
    result = Fraction(text)
    if abs(result.numerator) > MAX_INT or result.denominator > MAX_INT:
        raise ValueError("fraction bound exceeded")
    return result


def gold_channels(payload: dict[str, Any]) -> dict[str, Any]:
    """GOLD mean/zero-sum differences and Eisenstein cube projection."""
    values = _numbers(payload, "values", 6)
    if values is None:
        return _out("INVALID", reason="six bounded rational values required")
    mean = sum(values, Fraction(0)) / 6
    deltas = [v - mean for v in values]
    if sum(deltas, Fraction(0)) != 0:
        return _out("INVALID", reason="differences must sum to zero")
    # Optional explicit delta check catches mismatched caller reconstruction.
    explicit = payload.get("differences")
    if explicit is not None:
        supplied = _numbers({"differences": explicit}, "differences", 6)
        if supplied is None or supplied != deltas:
            return _out("INVALID", reason="supplied zero-sum differences do not match mean")
    vertices = payload.get("cube_vertices", [[x, y, z] for x in (0, 1) for y in (0, 1) for z in (0, 1)])
    if not isinstance(vertices, list) or len(vertices) != 8 or len({tuple(v) for v in vertices if isinstance(v, list)}) != 8 or any(not isinstance(v, list) or len(v) != 3 or any(x not in (0, 1) for x in v) for v in vertices):
        return _out("INVALID", reason="cube requires eight 3D vertices")
    fibers: dict[str, list[list[int]]] = {}
    for vertex in vertices:
        key = json.dumps([vertex[0] - vertex[2], vertex[1] - vertex[2]], separators=(",", ":"))
        fibers.setdefault(key, []).append(vertex)
    collision = any(len(v) > 1 for v in fibers.values())
    edge_pairs = []
    for i, left in enumerate(vertices):
        for j, right in enumerate(vertices[i + 1:], i + 1):
            if sum(a != b for a, b in zip(left, right)) == 1:
                edge_pairs.append((i, j))
    projected_edges = []
    for i, j in edge_pairs:
        projected_edges.append((json.dumps([vertices[i][0]-vertices[i][2], vertices[i][1]-vertices[i][2]]),
                                json.dumps([vertices[j][0]-vertices[j][2], vertices[j][1]-vertices[j][2]])))
    route = payload.get("route", {})
    area = None
    endpoints = payload.get("endpoints")
    paths = payload.get("compatible_paths")
    if isinstance(paths, list) and len(paths) == 2:
        endpoints = paths[0]
        try:
            if not paths[0] or not paths[1] or paths[0][0] != paths[1][0] or paths[0][-1] != paths[1][-1]:
                return _out("INVALID", reason="compatible paths must share start and end")
            def poly_area(path: list[Any]) -> Fraction:
                if len(path) < 2:
                    raise ValueError("a piecewise-linear path needs two points")
                return sum(_bounded_fraction(path[i][0]) * _bounded_fraction(path[(i+1)%len(path)][1]) - _bounded_fraction(path[(i+1)%len(path)][0]) * _bounded_fraction(path[i][1]) for i in range(len(path))) / 2
            area = str(poly_area(paths[0]) - poly_area(paths[1]))
        except (IndexError, TypeError, ValueError, ZeroDivisionError):
            return _out("INVALID", reason="compatible paths require finite rational pairs")
    elif isinstance(endpoints, list) and len(endpoints) >= 3:
        try:
            area = str(abs(sum(Fraction(str(endpoints[i][0])) * Fraction(str(endpoints[(i+1)%len(endpoints)][1])) - Fraction(str(endpoints[(i+1)%len(endpoints)][0])) * Fraction(str(endpoints[i][1])) for i in range(len(endpoints))) / 2))
        except (IndexError, TypeError, ValueError, ZeroDivisionError):
            return _out("INVALID", reason="endpoints must be finite rational pairs")
    sector = payload.get("sector", {})
    residual = payload.get("residual", {})
    if sector is not None and not isinstance(sector, dict):
        return _out("INVALID", reason="sector must be an object when supplied")
    if residual is not None and not isinstance(residual, dict):
        return _out("INVALID", reason="residual must be an object when supplied")
    sector_reconstruction = None
    if isinstance(sector, dict) and isinstance(residual, dict) and "base" in sector and "delta" in residual:
        try:
            sector_reconstruction = str(_bounded_fraction(sector["base"]) + _bounded_fraction(residual["delta"]))
        except (ValueError, TypeError, ZeroDivisionError):
            return _out("INVALID", reason="sector base and residual delta must be bounded rationals")
    turn = None
    if "n" in payload:
        try:
            n = int(payload["n"])
            if n < 0 or n > 1_000_000:
                raise ValueError
            if n == 0:
                k = 0
            else:
                def ge_k(candidate: int) -> bool:
                    A = 18*n + 1 - 2*candidate
                    return A >= 0 and A*A >= 180*n*n
                lo, hi = 0, 6*n + 1
                while lo + 1 < hi:
                    mid = (lo + hi)//2
                    if ge_k(mid): lo = mid
                    else: hi = mid
                k = lo
            eps = {"rational": f"{3*n}/2-{k}/6", "sqrt5_coefficient": f"{-n}/2"}
            turn = {"beta": "(3-sqrt(5))/2", "K": k, "j": k % 6,
                    "epsilon_turns": eps, "radians": "2*pi*epsilon_turns",
                    "floor_certificate": "integer_inequality", "abs_bound": "<1/12"}
        except (TypeError, ValueError, InvalidOperation):
            return _out("INVALID", reason="n must be bounded non-negative integer")
    return _out("PASS", channels=[str(x) for x in values], mean=str(mean), common_is_mean=True,
                differences=[str(x) for x in deltas], cube_vertices=vertices, cube_edges=len(edge_pairs),
                projection_fibers=fibers, edge_pairs=edge_pairs, projected_edges=projected_edges,
                edge_count=len(edge_pairs), projected_edge_count=len(set(projected_edges)),
                repair_bit="central_preimage" if collision else None,
                collision="COLLISION" if collision else "NONE", signed_route_area=area,
                endpoints=endpoints, compatible_paths=paths, route=route, sector=sector,
                residual=residual, sector_reconstruction=sector_reconstruction, beta_turn=turn,
                route_profile="piecewise_linear_signed_area_difference" if paths else None,
                route_exact_for_shared_endpoints=bool(paths),
                endpoint_vs_route=payload.get("endpoint_vs_route"),
                attribution=_source(payload))


def gppr_factor_events(payload: dict[str, Any]) -> dict[str, Any]:
    """Exact bounded symbolic factor/exponent event history."""
    factors = payload.get("factors", {})
    events = payload.get("events", [])
    if not isinstance(factors, dict) or len(factors) > MAX_ITEMS or not isinstance(events, list) or len(events) > MAX_ITEMS:
        return _out("INVALID", reason="bounded factors and events required")
    normalized = {}
    # p_j -> j.  GPPR's exact endpoint is indexed by registry position, not
    # by the numerical prime value.  A caller may extend this bounded fixture
    # with an explicit versioned registry.
    prime_indices = {2: 1, 3: 2, 5: 3, 7: 4, 11: 5, 13: 6, 17: 7, 19: 8,
                     23: 9, 29: 10, 31: 11, 37: 12, 41: 13, 43: 14,
                     47: 15, 53: 16, 59: 17, 61: 18, 67: 19, 71: 20,
                     73: 21, 79: 22, 83: 23, 89: 24, 97: 25, 101: 26,
                     103: 27, 107: 28, 109: 29, 113: 30, 127: 31, 131: 32}
    supplied_registry = payload.get("prime_registry", {})
    if not isinstance(supplied_registry, dict):
        return _out("INVALID", reason="prime_registry must map prime values to positive indices")
    try:
        for p, j in supplied_registry.items():
            if int(p) < 2 or int(j) < 1:
                raise ValueError
            prime_indices[int(p)] = int(j)
    except (TypeError, ValueError):
        return _out("INVALID", reason="prime_registry must map prime values to positive indices")
    product = 1
    prime_checked = True
    try:
        for prime, exponent in factors.items():
            p, e = int(prime), int(exponent)
            if p < 2 or p > MAX_INT or e < 0 or e > MAX_INT:
                raise ValueError
            # Certified factors are inputs: validate primality only within a
            # bounded trial-divisor budget; never factor an arbitrary target.
            if p > 2:
                root = int(p ** 0.5)
                if any(p % d == 0 for d in range(2, min(10000, root) + 1)):
                    raise ValueError("factor is composite")
                if root > 10000:
                    prime_checked = False
            if p not in prime_indices:
                return _out("INCOMPLETE", reason="prime registry index unavailable", prime=str(p))
            normalized[str(p)] = e
            if e >= 0 and e <= 100 and product <= MAX_INT:
                product *= p ** e
                if product > MAX_INT:
                    product = MAX_INT + 1
    except (TypeError, ValueError):
        return _out("INVALID", reason="integer factor/exponent bounds exceeded")
    declared_product = payload.get("product")
    if declared_product is not None:
        try:
            if int(declared_product) <= 0:
                return _out("INVALID", reason="target product must be positive integer")
        except (TypeError, ValueError):
            return _out("INVALID", reason="target product must be positive integer")
    product_match = declared_product is None or (product <= MAX_INT and str(product) == str(declared_product))
    if not product_match:
        return _out("INVALID", reason="factor product mismatch", factors=normalized, product=str(product))
    ordered = sorted(events, key=lambda x: (x.get("sequence", 0), str(x.get("event_id", ""))) if isinstance(x, dict) else (0, str(x)))
    chain = "0"; chain_records = []
    for event in ordered:
        encoded = json.dumps(event, sort_keys=True, separators=(",", ":"))
        chain = hashlib.sha256((chain + encoded).encode()).hexdigest()
        chain_records.append(chain)
    certified = product_match and (declared_product is not None) and product <= MAX_INT and prime_checked
    ribbon_counts: dict[str, int] = {}
    for event in ordered:
        if isinstance(event, dict) and "prime" in event:
            ribbon_counts[str(event["prime"])] = ribbon_counts.get(str(event["prime"]), 0) + int(event.get("multiplicity", 1))
    extra_events = sorted(set(ribbon_counts) - set(normalized))
    multiplicity_match = bool(ordered) and not extra_events and ribbon_counts == normalized
    certified = certified and multiplicity_match
    history_status = "VALIDATED" if ordered and multiplicity_match else "HISTORY_NOT_SUPPLIED"
    residual = None if certified else "prime/product/event history unresolved"
    endpoint_terms = [{"prime": p, "index": prime_indices[int(p)], "exponent": e,
                       "term": f"{e}*zeta^{prime_indices[int(p)]}"}
                      for p, e in sorted(normalized.items(), key=lambda item: prime_indices[int(item[0])])]
    return _out("PASS" if certified else "INCOMPLETE", factors=normalized, events=ordered,
                exact=True, certified=certified,
                certificate_status="FINITE_ARITHMETIC_CHECKED" if certified else "UNRESOLVED",
                product=str(product), event_multiplicity=ribbon_counts, extra_events=extra_events,
                multiplicity_match=multiplicity_match, history_status=history_status, integrity_chain=chain_records,
                endpoint_terms=endpoint_terms,
                residual=residual,
                attribution=_source(payload))


def gppr_partition(payload: dict[str, Any]) -> dict[str, Any]:
    """Route bounded two-dimensional enclosures through rectangular cells.

    This is a declared-geometry route only.  It never treats a supplied hash
    or boolean as a cryptographic enclosure certificate.
    """
    intervals = payload.get("enclosures", payload.get("intervals", []))
    cells = payload.get("cells", [])
    required = ("partition_id", "precision", "source_endpoint")
    missing = [x for x in required if x not in payload]
    if missing:
        return _out("INCOMPLETE", missing=missing, residual="partition binding unavailable")
    if not isinstance(intervals, list) or len(intervals) > MAX_ITEMS or not isinstance(cells, list) or len(cells) > MAX_ITEMS:
        return _out("INVALID", reason="bounded enclosures and versioned cells required")
    if payload.get("source_endpoint") in (None, "") or payload.get("precision") in (None, ""):
        return _out("INCOMPLETE", missing=["precision" if payload.get("precision") in (None, "") else "source_endpoint"], residual="endpoint binding or precision unavailable")

    def rectangle(value: Any, *, cell: bool = False) -> tuple[Decimal, Decimal, Decimal, Decimal] | None:
        if isinstance(value, dict):
            if "re" in value and "im" in value:
                re_pair, im_pair = value["re"], value["im"]
            elif all(k in value for k in ("re_lo", "re_hi", "im_lo", "im_hi")):
                re_pair, im_pair = [value["re_lo"], value["re_hi"]], [value["im_lo"], value["im_hi"]]
            else:
                return None
        elif isinstance(value, list) and len(value) == 4:
            re_pair, im_pair = value[:2], value[2:]
        else:
            return None
        if not isinstance(re_pair, (list, tuple)) or not isinstance(im_pair, (list, tuple)) or len(re_pair) != 2 or len(im_pair) != 2:
            return None
        try:
            out = tuple(Decimal(str(x)) for x in (re_pair[0], re_pair[1], im_pair[0], im_pair[1]))
        except (InvalidOperation, ValueError, TypeError):
            return None
        if not all(x.is_finite() for x in out) or out[0] > out[1] or out[2] > out[3]:
            return None
        return out

    # The old two-number interval shape remains a deliberately unresolved
    # fallback; GPPR routing requires a complex rectangle.
    if not isinstance(intervals, list) or any(rectangle(x) is None for x in intervals):
        return _out("FALLBACK", intervals=intervals, assignments=[None] * len(intervals) if isinstance(intervals, list) else [],
                    unresolved=intervals if isinstance(intervals, list) else [], conservative=True,
                    dimension="two-dimensional-required", certificate_verified=False,
                    residual="complex rectangular enclosure required", attribution=_source(payload))
    if not isinstance(cells, list) or len(cells) > MAX_ITEMS or any(rectangle(x, cell=True) is None for x in cells):
        return _out("INVALID", reason="cells require finite two-dimensional rectangles")
    parsed = [rectangle(x) for x in intervals]
    cell_rows = [(str(c.get("id", i)) if isinstance(c, dict) else str(i), rectangle(c, cell=True)) for i, c in enumerate(cells)]
    policy = payload.get("boundary_policy", "inclusive")
    if policy not in {"inclusive", "strict"}:
        return _out("INVALID", reason="boundary_policy must be inclusive or strict")
    assignments = []
    unresolved = []
    for row, enclosure in zip(intervals, parsed):
        if isinstance(row, dict) and "endpoint" in row and str(row["endpoint"]) != str(payload["source_endpoint"]):
            assignments.append(None); unresolved.append(row); continue
        matches = []
        for ident, cell in cell_rows:
            assert enclosure is not None and cell is not None
            if policy == "strict":
                inside = cell[0] < enclosure[0] and enclosure[1] < cell[1] and cell[2] < enclosure[2] and enclosure[3] < cell[3]
            else:
                inside = cell[0] <= enclosure[0] and enclosure[1] <= cell[1] and cell[2] <= enclosure[2] and enclosure[3] <= cell[3]
            if inside:
                matches.append(ident)
        if len(matches) == 1:
            assignments.append(matches[0])
        else:
            assignments.append(None); unresolved.append(row)
    supplied_metadata = bool(payload.get("enclosure_certificate")) and isinstance(payload.get("certificate_hash"), str)
    status = "ROUTED_UNDER_SUPPLIED_ENCLOSURE" if not unresolved else "FALLBACK"
    return _out(status, intervals=[list(map(str, x)) for x in parsed if x is not None], assignments=assignments,
                unresolved=unresolved, conservative=True, dimension="complex_rectangle",
                boundary_policy=policy, partition_id=payload["partition_id"], precision=payload["precision"],
                source_endpoint=payload["source_endpoint"], enclosure_assumption=True,
                certificate_metadata_present=supplied_metadata, certificate_verified=False,
                residual="enclosure crosses, misses cell, has endpoint mismatch, or is ambiguous" if unresolved else None,
                attribution=_source(payload))


TOOLS: dict[str, Callable[[dict[str, Any]], dict[str, Any]]] = {
    "science.observation_contract": observation_contract,
    "science.compare_prerequisites": compare_prerequisites,
    "science.detection_limit": detection_limit,
    "science.simulation_vs_observation": simulation_vs_observation,
    "science.residual_alternatives": residual_alternatives,
    "math.finite_endpoint": finite_endpoint,
    "math.readout_binding": readout_binding,
    "math.side_trace_repair": side_trace_repair,
    "math.apci_cost": apci_cost,
    "math.bridge_repair": bridge_repair,
    "math.gold_channels": gold_channels,
    "math.gppr_factor_events": gppr_factor_events,
    "math.gppr_partition": gppr_partition,
}

TOOL_DESCRIPTIONS = {name: fn.__doc__.split("\n")[0] for name, fn in TOOLS.items()}
