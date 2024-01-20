with open("all ^2, ^3, ^4, ^5 <= ten septillion.txt", "w") as f:
    for i in range(100001):
        for exponent in range(2, 6):
            f.write(f"{i:,}^{exponent} = {i**exponent:,}\n")
        
        
print("Done!")