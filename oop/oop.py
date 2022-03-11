#classes, creates objects
""" it describes what obj will be
classes are seperate from the objs
classes are objcs blurprint
we can use a class to make multiple objcs
data and function = attribute and method"""

class Cat:
#these are called class methods(which are funcs)
#init is called when an instance of
#an obj of the class is created,
#using the class name as function
	def __init__(self, color, legs):
		#color and legs are attributes of cat instan
		self.color = color
		self.legs = legs
felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)

print(rover.color)
print("-----------")
class Dog:
	def __init__(self, name, color):
		self.name=name
		self.color = color
	def bark(self):
		print("woof!")
fido = Dog("Fido", "brown")
print(fido.color)
fido.bark()
# cool.bark() will do error
print("-----------")
class Student:
	def __init__(self, name):
		self.name=name
	def saHi(self):
		print("Hi from " + self.name)
s1 = Student("Amy")
s1.saHi()
print("-----------")
# inheritance and SUPERCLASSES and subclasses
class Animal:
	def __init__(self, name, color):
		self.name=name
		self.color=color

class Cat(Animal):
	def purr(self):
		print("Purrr...")

class Dog(Animal):
	def Bark(self):
		print("Woooof!")
max = Dog("Max", "black")
print(felix.color)
felix = Cat("Felix", "ginger")
felix.purr()
print(felix.name)
print("-----------")
#subclass over ride superclass
class Wolf:
	def __init__(self, name, color):
		self.name=name
		self.color=color
	def bark(self):
		print("Grrrrrrrr...")
class Dog(Wolf):
	def bark(self):
		print("woof")
husky = Dog("max", "grey")
husky.bark()
# orride examples
class A:
	def spam(self):
		print(1)
class B(A):
	def spam(self):
		print(2)
		super().spam()
B().spam()
A().spam()
print("-----------")
""" operators(like + that is used by every method and
function)
Magic Methods/ dunders like __init__(for creating instace)
double underscore at end and beginnig
this enables to re define functions by user(operator
overloading )"""

class Vector2D:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def __add__(self, other):
		return Vector2D(self.x + other.x, self.y+other.y)
first = Vector2D(5, 7)
second = Vector2D(3, 9)
result= first + second
print(result.x)
print(result.y)
""" MAGIC METHODS:
__sub__ for -
__mul__ for *
__truediv__ for /
__floordiv__ for //
__mod__ for %
__pow__ for **
__and__ for &
__xor__ for ^
__or__ for |
add different types==> RADD
"""
# define a division operation
class SpecialString:
	def __init__(self, cont):
		self.cont = cont
	def __truediv__(self, other):
		line = "=" *len(other.cont)
		return "\n".join([self.cont, line, other.cont])

spam = SpecialString("spam")
hello = SpecialString("hello world!")
print(spam / hello)

#magic methods for comparisons:
"""__lt__ for <
__le__ for <=
__eq__ for ==
__ne__ for !=
__gt__ for >
__ge__ for >=

If __ne__ is not implemented, it returns the opposite of __eq__.
There are no other relationships between the other operators.
"""
class SpecialString:
	def __init__(self, cont):
		self.cont = cont

	def __gt__(self, other):
		for index in range(len(other.cont)+1):
			result = other.cont[:index] + ">" + self.cont
			result += ">" + other.cont[index:]
			print(result)
spam = SpecialString("spam")			
eggs = SpecialString("eggs")
spam > eggs

# Magic Methods for CONTAINERS:
"""__len__ for len()
__getitem__ for indexing
__setitem__ for assigning to indexed values
__delitem__ for deleting indexed values
__iter__ for iteration over objects (e.g., in for loops)
__contains__ for in

There are many other magic methods
"""

import random

class VagueList:
	def __init__(self, cont):
		self.cont = cont

	def __getitem__(self, index):
		return self.cont[index + random.randint(-1, 1)]
	def __len__(self):
		return random.randint(0, len(self.cont)*2)
vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[0])

# +++/// exersices \\\+++
# classes and instances
# attributes and methods = data and functions

class Employee:
	pass

"""different between class and an instance of a class,
+class = blueprint for creating instances
+instances = every(employee) that we make is an instace of that class

emp_1 = Employee()
emp_2 = Employee()

each of these is a unique(with diffrent address) instance of the Employee class
difference between instance variables and class variable

+instance variable: contains data that is unique to each instance

manual instances variable:

emp_1.first = "corey"
emp_1.last = "whatever"
emp_1.email ="whatever@company.com"

__init__ method is used to creat an automatic way to create instances
with their variables in a class
first argument that __init__ get has to be the instance itself
so we use (self):

    def __init__(self, first, last, pay):
    	self.first = first
    	self.last = last
    	self.pay = pay
    	self.email = first + "." + last + "@company.com"
emp_1 = Employee('name', 'last', 5000)
 
 if we want to add some actions:
 	1-manually
print('{} {}'.format(emp_1.first, emp_2.last))

 	2- add method to the our class
 	def fullname(self):
 		return '{} {}'.format(self.first, self.last)
print(emp_1.fullname())
+ we need parentheses because its a method not an attribute

+forgetting (self) argument in a method definition:
 err 
 instance will pass to a method as an argument automatically
 if we forget to write it in the defenition of the method
 an err will show that the method X 
 should have 0 arguments but 1 was given(1 being the instance)

    def fullname():
    	return '{} {}'.format(self.first, self.last)

  print(emp_1.fullname()) ===> err

emp_1.fullname() == Employee.fullname(emp_1)

first, last pay email are attributes of our Employee class

 +class variable:
 is the same for every instances of that class

"""
class Employee:
	rais_amount = 1.04
	emp_count = 0
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + "." + last + "@company.com"

		Employee.emp_count += 1

	def fullname(self):
		return "{} {}".format(self.first, self.last)

	def Raise(self):
		self.pay = int(self.pay * self.rais_amount)


emp_1 = Employee('corey', 'Schafer', 50000)
print(emp_1.__dict__)
emp_1.rais_amount = 0.5
print(emp_1.__dict__)
print(Employee.emp_count)
print(emp_1.emp_count)
print(Employee.__dict__)