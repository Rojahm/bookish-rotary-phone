#classes, creates objects
""" it describes what obj will be
classes are seperate from the objs
classes are objcs blurprint
we can use a class to make multiple objcs"""

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
