T = int(input())
coin = [25, 10, 5, 1]
	
for _ in range(T):
	change = int(input())
	count = []
	for i in range(len(coin)):
		count.append(change//coin[i])
		change = change%coin[i]
	
	print(*count)