from rps9 import rps
from guess_number import guess_number
import sys

def choose_game(name = "PlayerOne"):

    welcome_back = False

    while True:
        
        if welcome_back:
            print("\nWelcome back to the arcade!\n")

        
        choice = str(input(f"{name}, please type 1, 2, or x\n1 - Number Guessing Game\n2 - Rock Paper Scissors\nX - Quit\n")).lower()

        if choice not in ("1", "2", "x"):
            print("Please type 1, 2, or X.")
            return choose_game(name)

        welcome_back = True

        if choice == "1":
            guessing_game = guess_number(name)
            guessing_game()
        elif choice == "2":
            rps_game = rps(name)
            rps_game()
        else:
            print("Handle closing")
            sys.exit("Adios!")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personal greeting."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person to greet,"
    )

    args = parser.parse_args()
    name = args.name

    choose_game(name)