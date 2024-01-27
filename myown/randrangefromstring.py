from random import randint

while 1:
    inpt = input("String: ")
    
    r1 = randint(0, len(inpt) - 1)
    
    r2 = randint(r1, len(inpt) - 1)
    
    if r2 == len(inpt) - 1:
        r2 = None
    else: r2 +=1
        
    print(inpt[r1:r2])