N, K = map(int, input().split())
belt = list(map(int, input().split()))
robot = [0] * N

answer = 0
while True:
	answer += 1
	
	# [1] 벨트, 로봇 회전 & [N - 1] 로봇 내림
	belt = [belt[-1]] + belt[:-1]
	robot = [0] + robot[:-1]
	robot[N - 1] = 0

	# [2]
	for i in range(N-2, 0, -1):
		if robot[i] == 1 and robot[i + 1] == 0 and belt[i + 1] > 0:
			robot[i], robot[i + 1] = 0, 1
			belt[i + 1] -= 1
	
	# [3] 첫 번째 자리 내구도 > 0 이면 로봇 올림
	if belt[0] > 0:
		robot[0] = 1
		belt[0] -= 1
	
	# [4] 내구도 0인 개수 >= K 이면 탈출
	if belt.count(0) >= K:
		break

print(answer)