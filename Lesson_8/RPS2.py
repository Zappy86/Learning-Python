import random
import sys
from enum import Enum


class RPS(Enum):
    ROCK =  1
    PAPER = 2
    SCISSORS = 3

playagain = True

while playagain:

    # print(RPS(1)) gives ROCK
    # print(RPS.ROCK.value) gives 1

    print("\n")

    playerchoice = input("Enter ... \n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n")

    player = int(playerchoice)

    if player < 1 or player > 3:
        sys.exit("You must enter 1, 2, or 3.")

    computerchoice = random.choice("123")

    computer = int(computerchoice)

    print("\nYou chose " + str(RPS(player)).replace("RPS.", "") + ".")
    print("\nPython chose " + str(RPS(computer)).replace("RPS.", "") + ".")

    if player == 1 and computer == 3:
        print("🎉 You win!")
    elif player == 2 and computer == 1:
        print("🎉 You win!")
    elif player == 3 and computer == 2:
        print("🎉 You win!")
    elif player == computer:
        print("😲 Tie game!")
    else:
        print("🐍 Python wins!")

    playagain = input("\nPlay again?\nY for Yes or\nQ to Quit\n")

    if playagain.lower() == "y":
        continue
    else:
        print("\n🎉🎉🎉🎉🎉🎉")
        print("\nTHANKS FOR PLAYING!")
        playagain = False #you could also use break

sys.exit("Bye! 👋")