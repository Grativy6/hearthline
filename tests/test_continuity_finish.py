from hearthline_mcp.continuity import ContinuityEngine
from hearthline_mcp.store import SharedScopedStore

def engine(tmp_path):
    item = ContinuityEngine(SharedScopedStore(tmp_path, "finish-tests"))
    assert item.bind_tether({"tether_id":"t","task_id":"task","scope":"one","grant_ref":"g","finish_condition":"deliver receipt","residual":"review needed","return_target":"home"})["status"] == "BOUND"
    return item

def test_completion_report_never_reopens_on_creation_retry_or_resume(tmp_path):
    item = engine(tmp_path)
    request = {"heartbeat_id":"h","tether_id":"t","finish_condition":"deliver receipt","budget":5}
    item.create_heartbeat(request)
    assert item.pulse_heartbeat({"heartbeat_id":"h","event_id":"e","state":"COMPLETED"})["status"] == "COMPLETION_EVIDENCE_REQUIRED"
    pulse = {"heartbeat_id":"h","event_id":"e","state":"COMPLETED","finish_condition":"deliver receipt","completion_evidence_ref":"receipt1","cost":1}
    assert item.pulse_heartbeat(pulse)["status"] == "COMPLETED"
    assert item.create_heartbeat(request)["status"] == "COMPLETED"
    assert item.resume_heartbeat({"heartbeat_id":"h"})["status"] == "COMPLETED"
    assert item.pulse_heartbeat({**pulse,"completion_evidence_ref":"different"})["status"] == "IDEMPOTENCY_CONFLICT"
    assert item.read_heartbeat("h")["remaining"] == 4

def test_explicit_namespace_isolation(tmp_path):
    one, two = SharedScopedStore(tmp_path,"one"), SharedScopedStore(tmp_path,"two")
    one.append({"id":"same","content":"one"})
    assert two.read()["records"] == []
    assert one.namespace != two.namespace

def test_formation_requires_trio_and_separately_bound_completion(tmp_path):
    item = engine(tmp_path)
    base = {"formation_id":"f","source":"manifest1","grant_ref":"g","return_route":"controller","work":"one task","completion_keeper":"keeper","finish_condition":"deliver receipt"}
    members = [{"identity":identity,"role":role,"lane":"a","finish_condition":"deliver receipt","grant_ref":"g","return_route":"controller"} for identity,role in [("worker","worker"),("keeper","completion_keeper"),("ledger","ledger_keeper")]]
    assert item.validate_formation({**base,"members":members})["status"] == "VALID"
    assert item.validate_formation({**base,"members":members[:2]})["status"] == "INCOMPLETE"
    members[0]["identity"] = {}
    assert item.validate_formation({**base,"members":members})["status"] == "INCOMPLETE"

def test_invalid_current_observation_does_not_reopen(tmp_path):
    item = engine(tmp_path)
    grant = {"grant_ref":"g","task_id":"task","scope":"one","observed_at":"garbage","expires_at":"2099-01-01T00:00:00Z","revoked":False,"remaining_budget":1}
    assert item.reopen_tether({"tether_id":"t","current_grant":grant})["reopened"] is False

def test_trace_key_resolves_only_bound_scope(tmp_path):
    one = engine(tmp_path)
    key = one.prepare_trace_key({"record_id":"r","version":1,"source_hash":"sha256:"+"0"*64,"locators":["source1#section2"]})
    assert one.resolve_trace_key(key)["status"] == "RESOLVED"
    other = ContinuityEngine(SharedScopedStore(tmp_path, "other"))
    assert other.resolve_trace_key(key)["status"] == "CROSS_SCOPE_REJECTED"
    assert one.resolve_trace_key({**key,"source_hash":"changed"})["status"] == "SOURCE_CHANGED"
