import argparse

parser = argparse.ArgumentParser(
    description="Given a minimum and maximum range, and possibly a number, tries to guess that number",
    prog="Computer Guesses Number",
    epilog="Made by, once again, yours truly, the ever omniscient and omnibenevolent Dominic"
)

parser.add_argument(
    "-n", "--number", dest="number", type = int, metavar="number",
    help="The number given to be guessed, if not given it will choose one at random within bounds"
)

args = parser.parse_args()

if args.number == None:
    print("Banana")