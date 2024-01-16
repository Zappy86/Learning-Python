from random import shuffle, randint

#I could've done some closure stuff so that each time you ran the thing for it to guess it would guess a different one
#and then it handled all the printing and stuff on the outside but that seems too complex for something so simple
#and it probably isn't best practice anyways

#makes a sequence of every num in range, shuffles it, iterates through printing each time, and returns the given number when it finally reaches it
#it does *not* print the given number, only returns it
def comp_guess_num(min, limit, num):
    trials = 0

    sequence = list(range(min, limit + 1))
    shuffle(sequence)

    for x in sequence:
        if x == num:
            trials += 1
            return (num, trials)
        else:
            trials += 1
            print(f"It's not {x}")


if __name__ == "__main__":
    import argparse
    from sys import exit

    def parsing():
        
        parser = argparse.ArgumentParser(
            description="Given a minimum and maximum range, and possibly a number, tries to guess that number",
            prog="Computer Guesses Number",
            epilog="Made by, once again, yours truly, the ever omniscient and omnibenevolent Dominic"
        )

        parser.add_argument(
            "-m", "--minimum", required=True, type=int,
            help="The minimum integer the computer will be guessing"
        )

        parser.add_argument(
            "-l", "--limit", required=True, type=int,
            help="The maximum integer the computer will be guessing"
        )

        parser.add_argument(
            "-n", "--number", type = int,
            help="The number given to be guessed, if not given it will choose one at random within bounds"
        )

        args = parser.parse_args()

        if args.number == None: #if no number was given it chooses one randomly
            num = randint(args.minimum, args.limit)
        else:
            num = args.number
        
        #if the number is outside the range or the min and max are incorrect it stops
        if (args.limit < args.minimum):
            exit("You probably switched the minimum and limit, '-m' is minimum, '-l' is limit.")

        if (num < args.minimum) or (num > args.limit):
            exit("Chosen number is outside range.")

        return comp_guess_num(args.minimum, args.limit, num)
    
    result = parsing() #this will end up returning a tuple, (number it was guessing, # of trials)

    if result[0] not in (-666, -420, -69, -1, 0, 1, 42, 69, 100, 420, 666): #cheeky message for people who use common numbers, those ill-witted scallywags
        print(f"The number was '{result[0]:,}'!\nThat took {result[1]:,} trials!")
    else:
        print(f"The number was '{result[0]:,}'! (How original...)\nThat took {result[1]:,} Trials!")