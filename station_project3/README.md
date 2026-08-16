# Python Countdown Timer

## Description

This mini-project is a countdown timer written in Python.

The program asks the user to enter a time in the format:

```text
h:m:s
```

For example:

```text
0:5:32
```

The timer then counts down in the terminal, displaying a new line every second.


## How It Works

1. The user enters a time in `h:m:s` format.
2. The input string is split using `:`.
3. The three values are converted to integers.
4. The program checks that the input is valid.
5. The time is converted into total seconds.
6. A `while` loop counts down one second at a time.
7. `time.sleep(1)` pauses the program for exactly one second between countdown lines.
8. When the timer reaches `00:00:00`, the program prints `Time is up!`.


## Files

```text
station_project3/
├── timer.py
└── README.md
```

## How to Run

1. Clone the repository:
```bash 
git clone <my-repository-url>
cd <repository-folder>
```
2. Make sure Python is installed, then run:

```bash
python3 timer.py
```

3. Enter a time such as:

```text
0:5:32
```

## Example
<img width="895" height="618" alt="Screenshot 2026-08-13 at 17 28 54" src="https://github.com/user-attachments/assets/b0b5e44d-791c-4d65-8024-6bd51ba2d2cf" />


