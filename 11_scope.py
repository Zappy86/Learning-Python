name = "Dave"
count = 1

def another():
    color = "Blue"
    global count
    count += 1
    print(count)

    def greeting(name):
        print(color)
        print(name)

    greeting("Dave")

another()