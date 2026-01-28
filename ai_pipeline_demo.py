states = ["idle", "accelerating", "braking", "stuck", "recovering"]

for i, state in enumerate(states):
    if state == "stuck":
        print(f"Line {i}: AI detected stuck state → trigger recovery")
    else:
        print(f"Line {i}: AI state: {state}")