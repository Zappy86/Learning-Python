first = "Dominic"
last = "Murphy"

print(type(first))
print(type(first) == str)
print(isinstance(first, str))

#constructor function

pizza = str("Pepperoni")

print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

#Concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"

print(fullname)

print('')

#Multiple lines
multiline = '''
Hey, how're you?                            

I was just checking in :)        
                        You smell funny

'''

print(multiline)

#escaping special characters
sentence =  'I\'m pretty cool,\t'

#String Methods

print(first)
print(first.lower()) #all uppercase
print(first.upper()) #all lowercase
print(first)

print(multiline.title()) #capitalizes each word
print(multiline.replace("Hey", "Sup"))

print(len(multiline)) #counts blank space
multiline += "                                            "
multiline = "                       " + multiline #concatenates to beginning

print(len(multiline.strip())) #removes all white space
print(len(multiline.lstrip())) #removes white space from left side
print(len(multiline.rstrip()))

#Build a menu

title = "menu".upper()
print(title.center(20, "=")) #prints = signs around menu with the title in the middle
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))
#left/right justify, will print something like "Coffee................    $1"

print("")
#string index values
print(first[0]) #remember indexes start at 0
print(first[-1]) #gives last value in string
print(first[1:]) #if you don't provide the final value it will print all the way to the end

print("")

#methods that return boolean data
print(first.startswith("D"))
print(first.endswith("Z"))

#Boolean data type
myValue = True #has to be capitalized
x = bool(False) #constructor function
print(type(x))

#Complex numbers
comp_val = 5 + 3j
print(comp_val.real)
print(comp_val.imag)

gpa = 7.6

print(round(gpa)) #round to nearest int

print (round(gpa, 1)) #round to 1 decimal place


import math

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

#Cast string to number
zipcode = "10001"
zip_value = int(zipcode)