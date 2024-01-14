from random import shuffle

def Randtillsense(input):
    trials = 0
    oglist = list(input)
    coplist = oglist.copy()
    triallist = []
    
    shuffle(coplist)
    print("".join(coplist))
    triallist.append("".join(coplist))
    trials += 1

    while(coplist != oglist):
        shuffle(coplist)
        print("".join(coplist))
        triallist.append("".join(coplist))
        trials += 1

    triallist.append("".join(oglist))

    return(triallist, trials)

smallest = 99999999
smallestlist = []

for i in range(1000):
    new = Randtillsense("Dominic")
    if new[1] < smallest:
        smallest = new[1]
        smallestlist = new[0]

print("\n\n\n\n\n\n\nList:")

for item in smallestlist:
    print(item)

print(f"Smallest # of trials: {smallest}")