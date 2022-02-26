text = input()
dict = {}
#your code goes here
dict={i:text.count(i) for i in text if i!=' ' and i not in dict}
print(dict)