def calc(x):
    #your code goes here
    return (x*4, x**2)

side = int(input())
p, a = calc(side)

print("Perimeter: " + str(p))
print("Area: " + str(a))