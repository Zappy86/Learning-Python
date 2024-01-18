# squared = lambda num : num**2 #also called anonymous functions

# print(squared(5))

# addTwo = lambda num : num + 2

# print(addTwo(12))

# sum = lambda a, b : a + b

# print(sum(1, 2))

#####################################################

def funcBuilder(x):
    return lambda num : num + x

addten = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addten(5))
print(addTwenty(5))

#####################################################

numbers = [3, 7, 12, 18, 20, 21]

squared_nums = map(lambda num : num * num, numbers)

print(list(squared_nums))

#####################################################

lambda num : num % 2 != 0

odd_nums = filter(lambda num : num % 2 != 0, numbers)

print(list(odd_nums))

#####################################################

from functools import reduce

lambda acc, curr: acc + curr

numbers = [1, 2, 3, 4, 5, 1]

total = reduce(lambda acc, curr: acc + curr, numbers, 10)

print(total)

print(sum(numbers))




lambda acc, curr: acc + len(curr)

names = ["dave", "dom", "John jacob jingleheimerschmidt"]

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)

print(char_count)