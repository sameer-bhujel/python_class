#Assign string to a variable
a = "Hello world"
print(a)

#Multiline strings
x = """Hello everyone my name is sameer,
I live in Banepa, """
print(x)

#Strings and Arrays
a = "HelloWorld"
print(a[5])

#Looping through a String
for x in "Banepa":
  print(x)

#String length
a = "Hello IT-bridge"
print(len(a))

#check string
x = "My name is sameer"
print("Banepa" in x)

#Check if NOT
txt = "My name is sameer"
print("hello" not in txt)

#Slicing
b = "Hello World"
print(b[2:5])

#Slice from start
b = "Hello World"
print(b[:5])

#slice from end
b = "Hello World"
print(b[5:])


#Negative indexing
b = "Hello World"
print(b[-5:-2])

#UPPER CASE
a = "Hello World"
print(a.upper())

#lower case
a = "Hello World"
print(a.lower())


#Remove Whitespace
a = " Hello World    "
print(a.strip())


#Replacing string
a = "Hello World"
print(a.replace("H", "s"))


#Split string
a = "Hello, World"
b = a.split(",")
print(b)

#String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)


#String format
quantity = 5
itemno = 567
price = 1000
myorder = "I want {} pieces of item {} for {} rupees."
print(myorder.format(quantity, itemno, price))


#Escape Character
txt = "We are \"Banepali\" because we live in Banepa ."
print(txt)