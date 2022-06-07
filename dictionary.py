#dictionary
thisdict =	{
  "brand": "Ford",
  "model": "Mustang GT",
  "year": 1969
}
print(thisdict)

#Dictioinary item
thisdict = {
  "brand": "Ford",
  "model": "Mustang GT",
  "year": 1969
}
print(thisdict["model"])


#Duplication not allowed
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 1969
}
print(thisdict)

#Dictionary item-data types
thisdict = {
  "brand": "Ford",
  "electric": False,
  "diesel": True,
  "year": 1969,
  "colors": ["red", "blue"]
}

print(thisdict)


#type()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

#Get keys
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()

print(x)


#Get values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1969
}

x = thisdict.values()

print(x)


#get items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.items()

print(x)


#Check if key exist
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1969
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")



#Change value
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["year"] = 1969

print(thisdict)


#update dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1969
}
thisdict.update({"year": 2022})

print(thisdict)


#Adding items
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1969
}
thisdict["color"] = "black"
print(thisdict)


#Update dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1969
}
thisdict.update({"color": "red"})

print(thisdict)


#Removing items
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1969
}
thisdict.pop("model")
print(thisdict)


#loop dictionary
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])


#Copy dictionary
  thisdict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1969
  }
  mydict = thisdict.copy()
  print(mydict)


#Nested dictionary
child1 = {
  "name" : "saurav",
  "year" : 1998
}
child2 = {
  "name" : "sameer",
  "year" : 2007
}
child3 = {
  "name" : "ashok",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)




