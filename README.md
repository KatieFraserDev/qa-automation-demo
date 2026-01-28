# QA Automation Demo – AI State Validation

## Overview

This project is a lightweight QA automation demo that simulates testing
AI state transitions and log validation, inspired by game and AI-driven systems.

It demonstrates how automated tests can be used to detect invalid AI states
and verify recovery behavior when an AI enters a "stuck" condition.

## Project Structure

```text
qa-automation-demo/

├── ai\_pipeline\_demo.py      # Simulates AI state transitions

├── log\_checker.py           # Validates AI state logs

├── main.py                  # Core AI state processing logic

├── tests/

│   ├── test\_ai\_states.py    # Tests AI recovery behavior

│   └── test\_log\_checker.py  # Tests invalid log detection
```

## Technologies Used

* Python 3.x
* pytest
* Virtual environments (.venv)
* PyCharm

## Example Scenarios Tested

* Detection of invalid AI states in logs
* Verification of recovery behavior when AI enters a "stuck" state
* Validation of expected vs unexpected state transitions
