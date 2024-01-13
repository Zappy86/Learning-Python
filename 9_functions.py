def hello():
    print("Hello World!")

def sum(num1 = 0, num2 = 0): #you can set *default* values
    if (type(num1) is not int or type(num2) is not int):
        return #early return
    return num1 + num2

total = sum(1)
print(total)

def multiple_items(*args): #args is the common name, it represents the args as a tuple
    print(args)
    print(type(args))

multiple_items("Dave", "John", "Banana")


def mult_named_items(**kwargs): #stands for keyword arguments, will represents args as a dict
    print(kwargs)
    print(type(kwargs))

mult_named_items(first = "Dave", last = "Banana")