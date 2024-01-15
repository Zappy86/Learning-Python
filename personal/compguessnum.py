from random import shuffle, randint

#I could've done some closure stuff so that each time you ran the thing for it to guess it would guess a different one
#and then it handled all the printing and stuff on the outside but I'm not gonna be doing that right now

def choose_rand_num(min, limit):
    num = randint(min, limit)
    return num

def comp_guess_num(min, limit, num):
    sequence = []
    trials = 0

    for i in range(min, limit + 1): #choosing the num is inclusive, so this has to be too
        sequence.append(i) #makes a sequence out of every number in the given range
    
    shuffle(sequence) #shuffles up the sequence so its guesses are random

    for x in sequence: #returns the number when it finally gets to it
        if x == num:
            trials += 1
            return (num, trials)
        else:
            print(f"It's not {x}")
            trials += 1

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
            "-m", "--minimum", dest="minimum", required=True, type=int, metavar="minimum",
            help="The minimum integer the computer will be guessing"
        )

        parser.add_argument(
            "-l", "--limit", dest="limit", required=True, type=int, metavar="limit",
            help="The maximum integer the computer will be guessing"
        )

        parser.add_argument(
            "-n", "--number", dest="number", type = int, metavar="number",
            help="The number given to be guessed, if not given it will choose one at random within bounds"
        )

        args = parser.parse_args()

        if args.number == None: #if no number was given it chooses one randomly
            num = choose_rand_num(args.minimum, args.limit)
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
        print(f"The number is {result[0]:,}!\nThat took {result[1]:,} trials!")
    else:
        print(f"The number is {result[0]:,}! (How original...)\nThat took {result[1]:,} Trials!")