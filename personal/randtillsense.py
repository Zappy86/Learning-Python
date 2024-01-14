from random import shuffle

def Randtillsense(input):
    trials = 0
    oglist = list(input)
    coplist = oglist.copy()
    
    shuffle(coplist)
    print("".join(coplist))
    trials += 1

    while(coplist != oglist):
        shuffle(coplist)
        print("".join(coplist))
        trials += 1
    
    return["".join(coplist), trials]
        

if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(
        prog='Random until it makes sense',
        description='Shuffles the characters in a string until it outputs the original one',
        epilog='Created by yours truly, the ridiculously handsome and infinitely benevolent Dominic')

    parser.add_argument(
        "-i", "--input", dest="input", help="The string that halts the program when outputted", required=True, 
        type=str
    )

    args = parser.parse_args()

    result = Randtillsense(str(args.input))

    print(f"Final output: {result[0]}\nTrials: {result[1]}")