value = "y"
count = 0

while value:
    count += 1
    print(count)
    if(count == 5):
        break
    else:
        value = 0
        continue #you wouldn't need continue if there weren't anything afterward
