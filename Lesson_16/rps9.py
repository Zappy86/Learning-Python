import random
import sys
from enum import Enum

def rps(name="PlayerOne"):

    game_count = 0
    player_wins = 0
    computer_wins = 0
    tie_games = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal computer_wins
        nonlocal tie_games

        class RPS(Enum):
            ROCK =  1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input(f"\n{name}, please enter ... \n1 for Rock, \n2 for Paper, or \n3 for Scissors\n\n")

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            return play_rps() 

        player = int(playerchoice)

        computerchoice = random.choice("123")

        computer = int(computerchoice)

        print(f"\nYou chose {str(RPS(player)).replace("RPS.", "")}.")
        print(f"Python chose {str(RPS(computer)).replace("RPS.", "")}.")

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal computer_wins
            nonlocal tie_games
            nonlocal name

            if player == 1 and computer == 3:
                player_wins += 1
                return f"🎉 {name}, You Win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"🎉 {name}, You Win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"🎉 {name}, You Win!"
            elif player == computer:
                tie_games += 1
                return "😲 Tie game!"
            else:
                computer_wins += 1
                return f"🐍 Python wins!\nSorry, {name}...😟"

        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1
        print(f"\nGame count: {game_count}")
        print(f"{name}'s wins: {player_wins}")
        print(f"Computer wins: {computer_wins}")
        print(f"Tie games: {tie_games}")

        print(f"\nPlay again, {name}?\n")

        while True:
            playagain = input("Y for Yes or\nQ to Quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_rps()
        else:
            print("\n🎉🎉🎉🎉🎉🎉")
            print("\nTHANKS FOR PLAYING!")
            if __name__ == "__main__":
                sys.exit("Bye!")
            else:
                return
    return play_rps

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

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()