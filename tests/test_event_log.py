import json
from src.search import EventLog


def test_rotation_preserves_order_and_every_complete_record(tmp_path):
    log = EventLog(tmp_path, max_records=2)
    expected = [{"index": i, "status": "exact"} for i in range(5)]
    for record in expected:
        log.write(json.dumps(record) + "\n")
    log.close()
    paths = sorted(tmp_path.glob("events-*.jsonl"))
    assert len(paths) == 3
    assert [len(path.read_text().splitlines()) for path in paths] == [2, 2, 1]
    assert [json.loads(line) for path in paths for line in path.read_text().splitlines()] == expected
