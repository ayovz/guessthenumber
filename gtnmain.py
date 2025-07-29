import os
import random


ascii_art = """
  _____                   ________         _  __           __          
 / ___/_ _____ ___ ___   /_  __/ /  ___   / |/ /_ ____ _  / /  ___ ____
/ (_ / // / -_|_-<(_-<    / / / _ \/ -_) /    / // /  ' \/ _ \/ -_) __/
\___/\_,_/\__/___/___/   /_/ /_//_/\__/ /_/|_/\_,_/_/_/_/_.__/\__/_/   
                                                                       
"""

def get_number():
    return random.randint(1, 100)


replay = True

while replay:
    print(ascii_art)

    mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    x = 0

    if mode == 'easy':
        x = 10
        print("You have 10 attempts to guess the number.")
    elif mode == 'hard':
        x = 5
        print("You have 5 attempts to guess the number.")
    else:
        print("You've entered wrong difficulty.")

    number = get_number()

    for i in range(x):
        guess = int(input("Guess a number: "))

        if number > guess:
            print("Your guess is too low.\n")
            print(f"You have {x - i - 1} attempts to guess the number.")
        elif number < guess:
            print("Your guess is too high.\n")
            print(f"You have {x - i - 1} attempts to guess the number.")
        else:
            print(f"Your guess is correct. Correct answer is {number}.\n")

            print("Thanks for playing!\n")
            re = input("Do you want to play again? (y/n): ").lower()

            if re == 'y':
                replay = True
                os.system("cls")
            elif re == 'n':
                replay = False
            else:
                print("Thanks Again for playing!")

            break

