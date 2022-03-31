#sololearn easy exercises 

# Extra-Terrestrials

word = "hello"
i = len(word)
print(i)
while i > 0:
	print(word[i-1])
	i -= 1

# Fruit Bowl
num = 26
apples = num / 2
print(int(apples // 3))

# Cheer Creator
yards = int(input())
if yards > 10:
	print('High Five')
elif 0 <= yards and 10 >= yards:
	print('shh')
else:
	print('Ra!' * yards)

# Skee-Ball
score = int(input())
gun = int(input())
if int(score/12) >= gun:
	print("But it!")
else:
	print("Try again")