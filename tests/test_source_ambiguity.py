from hearthline_mcp.continuity import _source_check
from hearthline_mcp.core import digest


def test_duplicate_retrieval_and_binding_ids_remain_unverified():
    binding = {"source_id": "s", "version": "1", "hash": digest("source")}
    source = {"source_id": "s", "version": "1", "content": "source"}
    assert _source_check([binding], [source])[0] == "VERIFIED"
    assert _source_check([binding], [{**source, "content": "other"}, source])[0] == "UNVERIFIED"
    assert _source_check([binding, binding], [source])[0] == "UNVERIFIED"
