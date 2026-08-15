import random


def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2

    print("You rolled:", die1, "and", die2)
    print("Total:", total)

    return total


def play_craps():
    print("Welcome to the Craps Game!")
    print("Rolling the dice...")

    total = roll_dice()

    # First roll
    if total == 7 or total == 11:
        print("You win!")

    elif total == 2 or total == 3 or total == 12:
        print("Craps! The casino wins.")

    else:
        goal = total
        print("Your goal number is:", goal)
        print("Keep rolling!")

        while True:
            total = roll_dice()

            if total == goal:
                print("You rolled your goal number!")
                print("You win!")
                break

            elif total == 7:
                print("You rolled a 7!")
                print("You lose!")
                break

            else:
                print("Keep rolling...")


play_craps()
