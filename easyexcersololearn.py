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

#Paint costs
other = 40
color = 5
count = int(input())
import math
cost = (5 * count) + 40
tax = cost * 0.1
print(math.ceil(cost + tax))

# Argentina
pesos = int(input())
dollars = int(input())

if pesos * 0.02 < dollars:
	print("Pesos")
else:
	print("Dollars")

#Gotham City
criminals = int(input())
if criminals < 5:
	print('I got this!')
elif criminals >= 5 and criminals < 10:
	print('Help me Batman')
else:
	print('Good Luck out there!')

# Jungle Camping
noise = input()
for i in noise:
	if noise[i] == 'Grr':
		return 'Lion'
	elif noise[i] == 'Rawr':
		return 'Tiger'
	elif noise[i] == 'Ssss':
		return 'Snake'
	elif noise[i] == 'Chirp':
		return ' Bird'
	else:
		return 'No Animal'