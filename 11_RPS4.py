import random
import sys
from enum import Enum

game_count = 0

def play_rps():

    class RPS(Enum):
        ROCK =  1
        PAPER = 2
        SCISSORS = 3

        # print(RPS(1)) gives ROCK
        # print(RPS.ROCK.value) gives 1

    playerchoice = input("Enter ... \n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n")

    if playerchoice not in ["1", "2", "3"]:
        print("You must enter 1, 2, or 3.")
        return play_rps() #you can use recursion like this, it isn't expecting any output so this just runs everything again

    player = int(playerchoice)

    computerchoice = random.choice("123")

    computer = int(computerchoice)

    print("\nYou chose " + str(RPS(player)).replace("RPS.", "") + ".")
    print("\nPython chose " + str(RPS(computer)).replace("RPS.", "") + ".")

    def decide_winner(player, computer):
        if player == 1 and computer == 3:
            return "🎉 You win!"
        elif player == 2 and computer == 1:
            return "🎉 You win!"
        elif player == 3 and computer == 2:
            return "🎉 You win!"
        elif player == computer:
            return "😲 Tie game!"
        else:
            return "🐍 Python wins!"

    game_result = decide_winner(player, computer)
    print(game_result)

    global game_count
    game_count += 1
    print("Game count: " + str(game_count))

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
        sys.exit("Bye! 👋")

play_rps()