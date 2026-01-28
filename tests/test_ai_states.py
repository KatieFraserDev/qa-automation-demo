from main import process_ai_states

def test_process_ai_states(capfd):
    states = ["idle", "stuck", "accelerating"]
    process_ai_states(states)
    captured = capfd.readouterr()
    assert "AI detected stuck state → trigger recovery" in captured.out
