value = 1
while value <= 10:
    print(value)
    value += 1
else:
    print("The else ran") #WONT run if the loop breaks

names = ["Dom", "Mom", "Bom"]
for x in names:
    print(x)

for x in "Missippi":
    print(x)

for x in names:
    if x == "Sarah":
        break
    print(x)

for x in range(4):
    print(x)

for x in range(2,4):
    print(x)

for x in range(0, 100, 5): #increments by 5s
    print(x)
else:
    print("Glad that's over!")

names = ["Dom", "Mom", "Bom"]
actions = ["codes", "eats", "sleeps"]

for name in names:
    for action in actions:
        print(name + " " + action + ".")

print("\n\n")

for action in actions:
    for name in names:
        print(name + " " + action + ".")