#Dictionaries
band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))

# Access items in a dict
print(band["vocals"])
print(band.get("guitar"))

# List keys
print(band.keys())

#List all values
print(band.values())

# list of key/value pairs as tuples
print(band.items())

# verify key's existence
print("guitar" in band)
print("triangle" in band)
print("Plant" in band) #only checks keys

#change values
band["vocals"] = "Coverdale"
band.update({"bass":"JPJ"})
print(band)

#remove items
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem()) #removes last key value pair
print(band)

#Delete items

band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)
del band2

#Copy dict

# band2 = band does NOT creat a copy, makes a reference, referring to same place in memory <-- BAAAD

band2 = band.copy() #is the way to do it

#or use dict() constructor function
band3 = dict(band)

#Nested dictionaries

member1 = {
    "name": "Plant",
    "instrument":"vocals"
}
member2 = {
    "name": "page",
    "instrument":"guitar"
}

band = {
    "member1":member1,
    "member2":member2
}

print(band)
print(band["member1"]["name"])

#Sets
nums = {1, 2, 3, 4}

nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

#No duplicated allowed in sets
nums = {1, 2, 2, 4}
print(nums)

#True is a dupe of 1, and false is a dupe of 0
nums = {1, True, 4, False, 3, 2, 0}
print(nums)

#Check if value is in set
print(2 in nums)

#but you cannot refer to an element in the set with an index or key

#Add a new element to set
nums.add(8)
print(nums)

#add elements from one to another
morenums = {11, 24, 36}
nums.update(morenums)
print(nums)

#you can use update with lists, tuples, and dictionarties too
#data collection

#merge two sets to make one
one = {1, 2, 3}
two = {5, 6, 7}

mynewset = one.union(two)
print(mynewset)

#Keep only dupes
one = {1, 2, 3}
two = {5, 6, 3}
one.intersection_update(two) #updates one
print(one)

#Get rid of dupes,
one = {1, 2, 3}
two = {5, 6, 3}
one.symmetric_difference_update(two)
print(one) 