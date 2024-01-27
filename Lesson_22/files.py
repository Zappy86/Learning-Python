import os
# R - read
# A - append
# W - write
# X - create

# Equivalent in NoSQL:
# C - create
# R - read
# U - update
# D - delete

# Read - error if it doesn't exist, the default if a mode isn't specified

f = open("names.txt", "r")
# print(f.read())
# print(f.read(4))

# print(f.readline())
# print(f.readline())

for x in f:
    print(x)


f.close()

try:
    f = open("names.txt")
    print(f.read)
except:
    print("File doesn't exist.")
finally:
    f.close

# Append - creates the file if it doesn't exist

f = open("names.txt", "a")
f.write("Neil")
f.close()

f = open("names.txt")
print(f.read())
f.close()

# Write (overwrite)
f = open("context.txt", "w")
f.write("I deleted all of the context :)")
f.close()

f = open("context.txt")
print(f.read())
f.close()

# Two ways to make a new file

# Opens a file for writing, makes file if it doesn't exist
f = open("name_list.txt", "w")
f.close()

# Creates specified file, returns error if it exists
if not os.path.exists("dave.txt"):
    f = open("dave.txt", "x")
    f.close()
    
# Delete a file

# Avoid error if it doesn't exist
if os.path.exists("dave.txt"):
    os.remove("dave.txt")
else:
    print("File doesn't exist :()")
    
with open("more_names.txt") as f:
    content = f.read()

with open("names.txt", "w") as f:
    f.write(content)