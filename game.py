import random

ACTIONS = {0: "rock", 1: "paper", 2: "scissors"}

WINNING_MOVES = {"rock": "scissors", "paper": "rock", "scissors": "paper"}


def get_user_choice():
    while True:
        choices = [f"{ACTIONS[key]}[{key}]" for key in ACTIONS]
        print("Enter a choice:", ", ".join(choices))
        try:
            selection = int(input("> "))
            if selection in ACTIONS:
                return ACTIONS[selection]
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a number.")


def get_computer_choice():
    return random.choice(list(ACTIONS.values()))


def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif WINNING_MOVES[user] == computer:
        return "You win!"
    else:
        return "You lose."


if __name__ == "__main__":
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")
        print(determine_winner(user_choice, computer_choice))

        play_again = input("Play again? (y/n): ").lower()
        if play_again != "y":
            break
