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