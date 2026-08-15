# Station Project 1

## Description

Mad Libs is a word game where the player provides different types of words without knowing the final story. The program then places those words into a story template and displays the funny result.

This project is a Python console game based on the three Mad Libs templates provided in the assignment.

## Features

The program:

1. Shows three story templates.
2. Lets the user choose one template.
3. Asks the user for the required words and values.
4. Generates a complete story.
5. Prints the final story to the console.


## Files

```text
station_project1/
├── option1.py
├── option2.py
└── README.md
```

## How to Run

Make sure Python 3 is installed.

Open a terminal in the project folder and run:

```bash
python option1.py
```

On some systems, you may need:

```bash
python3 option1.py
```

## How to Play

When the program starts, you will see:

```text
Welcome to Python Station Project 1

Choose a story template:
1. Hospital
2. Camping
3. Enchanted Castle

Enter 1, 2, or 3: 
```

Enter the number of the story you want to play.

The program will then ask you for words such as:

```text
Type a noun:
Type an adjective:
Type a verb:
Type a color:
Type a number:
```

Enter any words you like. At the end, the program combines your answers into a funny story.


## Notes

The program intentionally keeps the game simple and uses only `print()`, `input()`, and functions created in the program for interaction, as requested by the assignment. The `random` library is also imported and used as required.
