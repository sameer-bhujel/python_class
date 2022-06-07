#sets
thisset = {"apple", "banana", "cherry"}
print(thisset)

#Duplicates not allowed
thisset = {"apple", "banana", "cherry", "apple", "apple", "banana", "mango"}

print(thisset)


#get the length of the sets
thisset = {"apple", "banana", "cherry", "apple", "apple", "banana", "mango"}

print(len(thisset))


#set item data types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)


#type
myset = {"apple", "banana", "cherry"}

print(type(myset))


#the set constructor
thisset = set(("1,2,3,4,5,6"))
print(thisset)

#Access items
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#Add items
thisset = {"car", "bike", "cycle"}

thisset.add("train")

print(thisset)


#Add sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)


#Add any iterable
thisset = {"apple", "banana", "cherry"}
mylist = ["bike", "bus"]

thisset.update(mylist)

print(thisset)


#remove set item
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana") #remove,discard

print(thisset)

##
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)


#Loop items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)


#join two sets
set1 = {"s", "a", "m"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#Keep only the duplicates
x = {"apple", "banana", "cherry"}
y = {"banana", "microsoft", "apple"}

x.intersection_update(y)

print(x)


#keep all but not duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)





