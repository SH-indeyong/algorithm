sec = [300, 60, 10]
	
time = int(input())
count = []
for i in range(len(sec)):
	count.append(time//sec[i])
	time = time%sec[i]

if time > 0:
	print(-1)
else:
	print(*count)