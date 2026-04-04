# Waiting Game

A simple Python console game that tests your internal timing!

## Description

The "Waiting Game" is a fun, lightweight script where the goal is to wait exactly 4 seconds between two key presses.

The game works as follows:

1. You run the script.
2. It prompts you to press `Enter` to start your timer.
3. You then wait, trying to estimate when exactly 4 seconds have passed.
4. You press `Enter` a second time to stop the timer.
5. The game will tell you exactly how accurate your internal clock was, indicating if you were perfectly on time, too fast, or too slow (with a precision of two decimal places).

## How to Run

To play the game, run the `wait_game.py` script using Python from your terminal or command prompt:

```bash
python wait_game.py
```

## Requirements

- Python 3.x
- No external libraries required. The script uses only the standard library's `time` module.
