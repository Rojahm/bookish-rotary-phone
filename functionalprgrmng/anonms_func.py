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