users = ["Dave", "Dominic", "Banana"]
emptylist = []

print("Dave" in users) #gives true

print(users[0])
print(users[-2])

print(users.index("Dominic"))

print(users[1:])

print(len(users))

users.append("Elsa")
print(users)

#next 2 have same functionality
users += ["Jason"]
#not equivalent to += "Jason", that will make a new element for each letter
print(users)

users.extend(["Robert", "Jimmy"])
print(users)

#next 2 have same functionality
users.insert(0, "Bob")
print(users)

users[2:2] = ["Eddie", "Alex"] #we're not actually replacing anything, the first element becomes the 2nd

users[1:3] = ["Robert", "JPJ"]
print(users) #this will replace values

users.remove("Dominic")
print(users)

print(users.pop()) #this will print the last value AND remove it
print(users)

del users[0] #deletes first element in list
print(users)

# del users would completely delete the list
# users.clear() replaces a list with an empty list

users[1:2] = ["elbert"]
users.sort()
print(users)

users.sort(key = str.lower)
print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)

nums.sort(reverse=True)
print(nums)

numcopy = nums.copy()
numcopy = list(nums)
numcopy = nums[:]

print(type(nums))

mylist = list([1, "Banana", True])

#Tuples! Order won't change and data won't change

mytuple = tuple(("7", "4", "4", "8"))
anothertuple = ("4", "5")

newlist = list(mytuple)
newlist.append(9807978)
newtuple = tuple(newlist)
print(newtuple)

#you can pack and UNPACK a tuple:
(one, *two, hey) = newtuple
print(one)
print(two)
print(hey)

print(newtuple.count("4"))