N = int(input())
K = int(input())
apple = [list(map(int, input().split())) for _ in range(K)]

# 사과 위치 표시: 1
arr = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
  for j in range(1, N + 1):
    if [i, j] in apple:
      arr[i][j] = 1

L = int(input())
move = [list(input().split()) for _ in range(L)]
for i in move:
  i[0] = int(i[0])

ci, cj = 1, 1
m = 0
d = 0
snake = [(1, 1)]
second = 0
#     동 남 서 북
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

while True:
  second += 1
  
  # 방향 변환해야 하는 경우
  if second == move[m][0] + 1:
    if move[m][1] == 'D':
      d = (d + 1) % 4
    else:
      d = (d - 1 + 4) % 4
    if m + 1 < len(move):
      m += 1

  ni, nj = ci + di[d], cj + dj[d]

  # 종료 조건
  if (ni, nj) in snake or ni <= 0 or ni > N or nj <= 0 or nj > N:
    # return
    break
  
  # 사과가 없는 경우
  if arr[ni][nj] == 0:
    snake.append((ni, nj))
    snake.pop(0)
  # 사과가 있는 경우
  else:
    arr[ni][nj] = 0
    snake.append((ni, nj))
    
  ci, cj = ni, nj

print(second)