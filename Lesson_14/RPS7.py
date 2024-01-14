import random
import sys
from enum import Enum

def rps():

    game_count = 0
    player_wins = 0
    computer_wins = 0
    tie_games = 0

    def play_rps():
        nonlocal player_wins
        nonlocal computer_wins
        nonlocal tie_games

        class RPS(Enum):
            ROCK =  1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input("Enter ... \n1 for Rock, \n2 for Paper, or \n3 for Scissors\n\n")

        if playerchoice not in ["1", "2", "3"]:
            print("You must enter 1, 2, or 3.")
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

            if player == 1 and computer == 3:
                player_wins += 1
                return "🎉 You win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return "🎉 You win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return "🎉 You win!"
            elif player == computer:
                tie_games += 1
                return "😲 Tie game!"
            else:
                computer_wins += 1
                return "🐍 Python wins!"

        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1
        print(f"\nGame count: {str(game_count)}")
        print(f"Player wins: {str(player_wins)}")
        print(f"Computer wins: {str(computer_wins)}")
        print(f"Tie games: {str(tie_games)}")

        print("\nPlay again?\n")

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
            sys.exit("Bye!👋\n\n\n")
    return play_rps

rock_paper_scissors = rps()

if __name__ == "__main__":
    rock_paper_scissors()