import random


def roll_dice():
    """Rolls two 6-sided dice, displays their values, and returns the total sum."""
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    print(f"You rolled {die1} and {die2} | Total: {total}")
    return total


def play_craps():
    """Main game logic controlling the rules, loops, and game state."""

    instant_win = [7, 11]
    instant_loss = [2, 3, 12]

    print(" Welcome to the Craps Game!")
    print("Rolling the dice for the first turn...\n")

    first_roll = roll_dice()

    # First roll evaluations
    if first_roll in instant_win:
        print("\nCongratulations! You rolled a natural win!")
        return
    elif first_roll in instant_loss:
        print("\nCraps! The casino wins.")
        return
    else:
        goal = first_roll
        print(f"\nYour goal number is set to: {goal}")
        print("Keep rolling until you hit your goal to win, or roll a 7 to lose.\n")

    
    game_over = False
    while not game_over:
        input("Press Enter to roll again...")
        current_roll = roll_dice()

        if current_roll == goal:
            print(f"\nYou hit your goal number ({goal})! You win!")
            game_over = True
        elif current_roll == 7:
            print("\nYou rolled a 7 before reaching your goal. The casino wins!")
            game_over = True


if __name__ == "__main__":
    play_craps()