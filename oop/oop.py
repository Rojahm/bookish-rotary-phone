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
