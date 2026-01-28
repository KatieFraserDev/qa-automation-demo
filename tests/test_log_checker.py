from log_checker import find_invalid_states

def test_find_invalid_states():
    logs = ["idle", "accelerating", "teleporting", "braking", "hovering"]
    invalid = find_invalid_states(logs)
    assert invalid == ["teleporting", "hovering"]
