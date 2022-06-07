#print using for loop
mountains = ["Everest", "Ganesh", "Langtang"]
for x in mountains:
  print(x)


#Looping through string
for x in "HelloiyIT-Briidge":
  print(x)


#The Break statement
mountains = ["Everest", "Ganesh", "Langtang"]
for x in mountains:
  print(x)
  if x == "Ganesh":
   break


#the cotinue statement
mountains = ["Everest", "Ganesh", "Langtang"]
for x in mountains:
  if x == "Ganesh":
  	continue
  print(x)


#the renge()function
for x in range(1, 11):
  print(x)


#else in For loop
for x in range(1, 11):
  print(x)
else:
  print("Finally finished.")


#Nested loop
adj = ["red", "amazing", "sport"]
fruits = ["car", "bike", "cycle"]

for x in adj:
  for y in fruits:
    print(x, y)



