# -*- coding: utf-8 -*-
"""
w3 school
"""


# loop while

i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  
# Note that number 3 is missing in the result

"""
The else Statement
With the else statement we can run a block 
of code once when the condition no longer is true:

Example
Print a message once the condition is false:
    
"""
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
  

####################################################
#       loop for                                   #
####################################################

for x in "banana":
  print(x) 
  
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
      break
  print(x)
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
  
for x in range(2, 30, 3):
  print(x)


# Else in For Loop

#1
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#2
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#3
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#4    
"""
Arbitrary Arguments, *args
If you do not know how many arguments that will 
be passed into your function, add a * before the
 parameter name in the function definition.

This way the function will receive a tuple of arguments
, and can access the items accordingly:
Example
If the number of arguments is unknown, add a * before 
the parameter name:
    
"""

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#5
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#6
"""
Arbitrary Keyword Arguments, **kwargs
If you do not know how many keyword arguments that
 will be passed into your function, 
 add two asterisk: ** before the parameter name in 
 the function definition.

This way the function will receive a dictionary of
 arguments, and can access the items accordingly:

Example
If the number of keyword arguments is unknown, add a
 double ** before the parameter name:
"""

#6
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))



##################################################
#          Array                                 #
##################################################

cars = ["Ford", "Volvo", "BMW"]

x = cars[0]

print(x)

cars[0] = "Toyota"

x = cars[0]

cars

print(x)



#################################################
#       Python Classes and Objects              #
#################################################

"""
Python Classes/Objects
Python is an object oriented programming language.

Almost everything in Python is an object, with its 
properties and methods.

A Class is like an object constructor, or a "blueprint"
 for creating objects.
 
"""
 
#1
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age) 


#2
"""
The __str__() Function
The __str__() function controls what should be returned
 when the class object is represented as a string.

If the __str__() function is not set, the string
 representation of the object is returned:

Example
The string representation of an object WITHOUT
the __str__() function:     
"""

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

Person("John", 36)
print(p1)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"    

p1 = Person("John", 36)

print(p1)


#3
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()


######################################################
#                 Python Inheritance                 #
#                 Python Inheritance                 #
#    Inheritance allows us to define a class that    # 
#    inherits all the methods and properties from    #
#    another class.                                  #
#                                                    #
#  Parent class is the class being inherited from,   #
#  also called base class.                           #
#                                                    #
#  Child class is the class that inherits from       #
#  another class, also called derived class.         #
#                                                    #
#  Create a Parent Class                             #
#  Any class can be a parent class, so the syntax is #
#  the same as creating any other class:             #
#                                                    #
#  Create a class named Person, with firstname and   #
#  lastname properties, and a printname method:      #
######################################################

#1
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()


#2
"""
Use the super() Function
Python also has a super() function that will make 
the child class inherit all the methods and properties
 from its parent:
"""

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Mike", "Olsen")
x.printname()

#3
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

x = Student("Mike", "Olsen")
print(x.graduationyear)

#4
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()


########################################################
#            Python Iterators                          #
########################################################

#1
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

#2 
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#3 Looping Through an Iterator

"""
Looping Through an Iterator
We can also use a for loop to iterate through an
iterable object:

Example
Iterate the values of a tuple:
"""
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
  

###############################################
#               Class Polymorphism
###############################################

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
  x.move()
  

#2
"""
Inheritance Class Polymorphism
"""

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()
  
########################################################
# module
########################################################  
 
#1 
import mymodule

a = mymodule.person1["age"]
print(a)

#2
from mymodule import person1

print (person1["age"])


#######################################################
# DATE
#######################################################

#1
import datetime

x = datetime.datetime.now()
print(x)

#2
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

#3
import datetime

x = datetime.datetime(2020, 5, 17)

print(x)

#4
import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))


#######################################################
#    JSON
#######################################################

#1
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])


#2

#Convert from Python to JSON:

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

#3
#Convert Python objects into JSON strings, and print the values:

import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

#4
#Convert a Python object containing all the legal data types:

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

#5
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))


#2
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
print(json.dumps(x, indent=4, separators=(". ", " = ")))

#3
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# sort the result alphabetically by keys:
print(json.dumps(x, indent=4, sort_keys=True))


##############################################
# MySQL and PYTHON
##############################################

#1
import mysql.connector



mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="#k41W146)"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
  
  
# 2
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="#k41W146)",
  database="e_commerce"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)
  
#3 create table
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

mycursor.execute("select * from paiment")
for x in mycursor:
  print(x)

#4 Python MySQL Insert Into Table

#4-1
mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

#4-2 insert multiple raw
mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")

# Get Inserted ID

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)

#4-3 Python MySQL Select From

#a
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  
#b  
mycursor = mydb.cursor()

mycursor.execute("SELECT name, address FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  
#c
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchone()

print(myresult)