# c = 구름, n = next, 
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cloud = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]

di = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dj = [0, -1, -1, 0, 1, 1, 1, 0, -1]

for _ in range(M):
  d, s = map(int, input().split())
  next_cloud = []

  # [1] 구름 이동 [2] 물 1 증가 [3] 구름 증발 위치 저장
  for ci, cj in cloud:
    ni, nj = (ci + di[d] * s + N) % N, (cj + dj[d] * s + N) % N
    arr[ni][nj] += 1
    next_cloud.append((ni, nj))

  # [4] 4 방향의 대각선에 물 있는 칸 수만큼 물 증가
  visit = [[0] * N for _ in range(N)]
  for ci, cj in next_cloud:
    visit[ci][cj] = 1
    for dd in (2, 4, 6, 8):
      ni, nj = ci + di[dd], cj + dj[dd]
      if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] > 0:
        arr[ci][cj] += 1

  # 전체 순회하면서 물이 2 이상인 칸 구름 발생 ---> 물 -= 2
  cloud = []
  for i in range(N):
    for j in range(N):
      if arr[i][j] >= 2 and visit[i][j] == 0:
        arr[i][j] -= 2
        cloud.append((i, j))

water = 0
for i in arr:
  water += sum(i)
print(water)