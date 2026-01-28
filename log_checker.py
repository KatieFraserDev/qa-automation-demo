def find_invalid_states(log_lines):
    valid_states = {"idle", "accelerating", "braking", "recovering"}
    invalid = []

    for line in log_lines:
        if line not in valid_states:
            invalid.append(line)

    return invalid


sample_logs = [
    "idle",
    "accelerating",
    "teleporting",
    "braking",
    "hovering"
]

print(find_invalid_states(sample_logs))
