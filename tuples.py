#Tuples
thistuple = ("bike", "bus", "car")
print(thistuple)


#It allow duplication
thistuple = ("bus", "bike", "car", "bus", "car")
print(thistuple)


#Tuple lenth
thistuple = tuple(("car", "bus", "jeep", "bike"))
print(len(thistuple))

#tuple item - data types
tuple1 = ("car", "bus", "bike")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)

#type()
mytuple = ("car", "bus", "bike")

print(type(mytuple))

#the tuple constructor
thistuple = tuple(("car", "bike", "car"))
print(thistuple)


#access tuple item
thistuple = ("car", "bike", "gun")
print(thistuple[1])

#Negative indexing
thistuple = ("school", "medical", "shop")
print(thistuple[-1])

#Range of indexing
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])


#Range of negative indexing
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])


#check if item exists
thistuple = ("car", "bus", "bike")
if "bus" in thistuple:
  print("Yes, 'bus' is in the vehicle tuple")


#change tuple values
x = ("car", "bus", "jeep")
y = list(x)
y[1] = "sedan"
x = tuple(y)

print(x)

#Add item
thistuple = ("bus", "bike", "car")
y = list(thistuple)
y.append("train")
thistuple = tuple(y)

print(thistuple)


#remove items
thistuple = ("bike", "bus", "car", "cycle")
y = list(thistuple)
y.remove("cycle")
thistuple = tuple(y)

print(thistuple)


#Unpack a tuple
vehicle = ("car", "bus", "bike")

(green, yellow, red) = vehicle

print(green)
print(yellow)
print(red)


#using Asterisk*
vehicle = ("car", "bike", "cycle", "bus", "train")

(green, *tropic, red) = vehicle

print(green)
print(tropic)
print(red)


#loop through touple
thistuple = ("car", "bus", "bike")
for x in thistuple:
  print(x)


#loop through indexing numbers
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[1])


#using a while loop
thistuple = ("car", "bus", "cycle", "bike")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1


#join two touples
tuple1 = ("car", "bus" , "cycle")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


#multiply tuples
fruits = ("car", "bike", "bus", "train")
mytuple = fruits * 3

print(mytuple)
