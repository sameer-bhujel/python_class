# List simple example
list = ["bus", "bike", "car"]
print(list)


#List item  - data types
list1 = ["car", "bus", "bike"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

#List Type()
mylist = ["bus", "bike", "car"]

print(type(mylist))

#Access list items
thislist = ["Ram", "Balram", "Gopal"]
print(thislist[1])


#Negative Indexing
thislist = ["Ram", "Balram", "Gopal"]
print(thislist[-1])

#Range of indexing
thislist = ["Ram", "Balram", "Gopal", "Hari", "Sita", "Milan", "Manoj"]
print(thislist[2:5])

#Change item value
thislist = ["Ram", "Balram", "Gopal", "Hari", "Sita", "Milan", "Manoj"]
thislist[1] = "Sameer"
print(thislist)


#Change a range of Item Values
thislist = ["Ram", "Balram", "Gopal", "Hari", "Sita", "Milan", "Manoj"]
thislist[1:3] = ["Bishal", "Ujjwol"]
print(thislist)

#Insert item
thislist = ["bike", "bus", "car"]

thislist.insert(2, "plane")

print(thislist)

#Add list in item
#Append Items
thislist = ["apple", "banana", "cherry"]

thislist.append("orange")

print(thislist)

#insert item
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)


#Extend list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]

thislist.extend(tropical)

print(thislist)


#Add any Iterable
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")

thislist.extend(thistuple)

print(thislist)


#Remove specified item
thislist = ["bus", "bike", "car"]
thislist.remove("bus")
print(thislist)


#Remove specified index
thislist = ["bike", "bus", "car"]
thislist.pop(1)
print(thislist)


#clear the list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#List comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


#short list numerically
thislist = [100, 50, 65, 82, 23]

thislist.sort()

print(thislist)


#short list alphabetically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

thislist.sort()

print(thislist)


#Short descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

thislist.sort(reverse = True)

print(thislist)


#customze short function
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]

thislist.sort(key = myfunc)

print(thislist)

#Reverse order
thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.reverse()

print(thislist)


#copy list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


#join list
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

