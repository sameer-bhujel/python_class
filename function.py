#Creating function
def my_function():
  print("Hello from a Banepa")

my_function()



#Arguments
def my_function(fname):
  print(fname + " Thapa")

my_function("Lynux")
my_function("Java")
my_function("Python")



#Number of Arguments
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Sameer", "Bhujel")



#Abitrary Arguments, *args
def my_function(*kids):
  print("The youngest child is " + kids[0])

my_function("Ram", "Sham", "Hari")



#Keyword Arguments
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Hari", child2 = "Sham", child3 = "Sagar")


#Abitrary keyword arguments, **kwargs
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Hari", lname = "Thapa")


# Default Parameter value
def my_function(country = "Bagmati"):
  print("I am from " + country)

my_function("Banepa")
my_function("Kavre")
my_function()
my_function("Nepal")


#passing a list as an argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)



#Return value
def my_function(x):
  return 10 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


#Recursion



