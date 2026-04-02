import random

VALID_CHOICES = ['rock', 'paper', 'scissors']

# Maps each choice to the choice it beats
WINS_AGAINST = {
    'rock': 'scissors',
    'scissors': 'paper',
    'paper': 'rock',
}


def validate_choice(choice):
    """Return True if choice is one of 'rock', 'paper', or 'scissors'."""
    return choice in VALID_CHOICES


def get_computer_choice():
    """Return a random choice of 'rock', 'paper', or 'scissors'."""
    return random.choice(VALID_CHOICES)


def determine_winner(user_choice, computer_choice):
    """Return a string describing the result of the round.

    Possible return values:
      "It's a tie!"        — both players chose the same option
      "You win! <detail>"  — user_choice beats computer_choice
      "Computer wins! <detail>" — computer_choice beats user_choice
    """
    if user_choice == computer_choice:
        return "It's a tie!"

    if WINS_AGAINST[user_choice] == computer_choice:
        return (
            f"You win! {user_choice.capitalize()} beats "
            f"{computer_choice.capitalize()}."
        )

    return (
        f"Computer wins! {computer_choice.capitalize()} beats "
        f"{user_choice.capitalize()}."
    )
