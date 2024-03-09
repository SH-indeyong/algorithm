change = 1000 - int(input())
count = 0

coin = [500, 100, 50, 10, 5, 1]

while change > 0:
	for i in range(len(coin)):
		while change >= coin[i]:
			change -= coin[i]
			count += 1

print(count)