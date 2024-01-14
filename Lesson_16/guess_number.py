import random
import sys

def guess_number(name = "PlayerOne"):

    #if these variables were inside the play function they'd be reinitialized everytime, we could make them global variables but we don't want to clutter it up

    game_count = 0
    player_wins = 0
    computer_wins = 0

    def play_guess_number():
        nonlocal name
        nonlocal game_count
        nonlocal player_wins
        nonlocal computer_wins

        playerchoice = input(f"\n{name}, please guess a number... 1, 2, or 3\n")

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            return play_guess_number() 

        player = int(playerchoice)

        computer = int(random.choice("123"))

        print(f"\nYou chose {player}.")
        print(f"Python chose {computer}.")

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal computer_wins
            nonlocal name

            if player == computer:
                player_wins += 1
                return f"🎉 {name}, You Win!"
            else:
                computer_wins += 1
                return f"🐍 Python wins!\nSorry, {name}...😟"

        game_result = decide_winner(player, computer)
        print(game_result)

        game_count
        game_count += 1
        print(f"\nGame count: {game_count}")
        print(f"{name}'s wins: {player_wins}")
        print(f"Computer wins: {computer_wins}")
        print(f"You're win percent: {player_wins/game_count:.2%}")

        print(f"\nPlay again, {name}?\n")

        while True:
            playagain = input("Y for Yes or\nQ to Quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_guess_number()
        else:
            print("\n🎉🎉🎉🎉🎉🎉")
            print("\nTHANKS FOR PLAYING!")
            if __name__ == "__main__":
                sys.exit()
            else:
                return
    return play_guess_number

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()

    guess_my_number = guess_number(args.name)
    guess_my_number()