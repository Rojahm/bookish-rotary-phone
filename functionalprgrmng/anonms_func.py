def  my_func(f, arg):
	return f(arg)
a= my_func(lambda x: 2*x*x, 5)
print(a)
b= (lambda x: x*x)(8)
print(b) 

"""map 
&
filter"""

def add_five(x):
	return x+5
nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)

nums = [11, 22, 33, 44, 55]
result = list(map(lambda x: x+5, nums))
print(result)

nums = [11, 22, 33]
a = list(map(lambda x: x*2, nums))
print(a)

nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x % 2 ==0, nums))
print(res)

#generators
def countdown():
	i = 5
	while i>0:
		yield i
		i -= 1
for i in countdown():
	print (i)

def numbers (x):
	for i in range(x):
		if i % 2 ==0:
			yield i

print(list(numbers(11)))

def make_word():
	word=""
	for ch in "spam":
		word += ch
		yield word
print(list(make_word()))

#decor function 
"""it is a function that would change other 
functions"""
def decor(func):
	def wrap():
		print("==========")
		func()
		print("==========")
	return wrap
@decor
def print_text():
	print("Hello world!")
decorated = decor(print_text)
decorated()


#recursion- tavabe baazgashti
#classic factorial x!
""" in this case 1 is the base case result
which acts as the exit condition of the recursion
without it infinite function calls results 
crashing the program"""

def factorial(x):
	if x==1:
		return 1
	else:
		return x * factorial(x-1)
print(factorial(5))

# indirect recursion

def is_even(x):
	if x==0:
		return True
	else:
		return is_odd(x-1)
def is_odd(x):
	return not is_even(x)
print(is_odd(17))
print(is_even(23))

#fib func
def fib(x):
	if x==0 or x==1:
		return 1
	else:
		return fib(x-1) +fib(x-2)
print(fib(4))
print("-------------")
#*args
def function2(named_arg, *args):
	print(named_arg)
	print(args)
function2(1, 2, 3, 4, 5)
print("-------------")


