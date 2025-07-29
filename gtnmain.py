import os
import random

# ASCII Art Title
ascii_art = """
  _____                   ________         _  __           __          
 / ___/_ _____ ___ ___   /_  __/ /  ___   / |/ /_ ____ _  / /  ___ ____
/ (_ / // / -_|_-<(_-<    / / / _ \/ -_) /    / // /  ' \/ _ \/ -_) __/
/___/\_,_/\__/___/___/   /_/ /_//_/\__/ /_/|_/\_,_/_/_/_/_.__/\__/_/   

"""


def clear_screen():
    """Clears the terminal screen (cross-platform)."""
    os.system('cls' if os.name == 'nt' else 'clear')


def get_random_number():
    """Returns a random integer between 1 and 100."""
    return random.randint(1, 100)


def choose_difficulty():
    """
    Prompts the user to choose a difficulty level.
    Returns the number of attempts based on choice.
    """
    while True:
        mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if mode == 'easy':
            print("You have 10 attempts to guess the number.")
            return 10
        elif mode == 'hard':
            print("You have 5 attempts to guess the number.")
            return 5
        else:
            print("Invalid input. Please type 'easy' or 'hard'.")


def get_user_guess():
    """Prompts the user to enter a valid number between 1 and 100."""
    while True:
        try:
            guess = int(input("Guess a number (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def play_game():
    """Main game logic."""
    print(ascii_art)
    attempts = choose_difficulty()
    secret_number = get_random_number()

    for attempt in range(attempts):
        guess = get_user_guess()

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"🎉 Correct! The number was {secret_number}.")
            return True  # Win

        remaining = attempts - attempt - 1
        if remaining > 0:
            print(f"You have {remaining} attempts left.\n")
        else:
            print(f"\n❌ You're out of guesses. The correct number was {secret_number}.")
            return False  # Loss


def ask_to_replay():
    """Asks the user if they want to play again. Returns True/False."""
    while True:
        choice = input("Do you want to play again? (y/n): ").lower()
        if choice == 'y':
            clear_screen()
            return True
        elif choice == 'n':
            print("Thanks for playing! 👋")
            return False
        else:
            print("Please enter 'y' or 'n'.")


def main():
    """Entry point for the number guessing game."""
    replay = True
    while replay:
        play_game()
        replay = ask_to_replay()


if __name__ == "__main__":
    main()
