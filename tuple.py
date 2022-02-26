contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]
dic = dict(contacts)
print(dic)
name = input()
age=dic.get(name, 'Not found')
if age != 'Not found':
    print(name+' is '+str(age))
else:
    print('Not found')
