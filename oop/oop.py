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
