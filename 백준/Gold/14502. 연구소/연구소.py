from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

vacant = []
virus = []

for i in range(N):
  for j in range(M):
    if arr[i][j] == 0:
      vacant.append((i, j))
    elif arr[i][j] == 2:
      virus.append((i, j))

def bfs(build):
  # [1] 선택한 좌표에 벽 설치
  for i, j in build:
    arr[i][j] = 1
  
  # [2] 큐 생성 및 초기화
  q = deque()
  visit = [[0] * M for _ in range(N)]
  count = COUNT - 3       # 남은 빈 칸 수

  for vi, vj in virus:
    q.append((vi, vj))
    visit[i][j] = 1
  
  # [3] 바이러스 확산: 큐에 데이터가 존재하는 동안 한 개씩 꺼내서 실행
  while q:
    ci, cj = q.popleft()  # 바이러스 좌표
    for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
      ni, nj = ci + di, cj + dj
      if 0 <= ni and ni < N and 0 <= nj and nj < M and arr[ni][nj] == 0 and visit[ni][nj] == 0:
        q.append((ni, nj))
        visit[ni][nj] = 1
        count -= 1
  
  # [4] 원상태
  for i, j in build:
    arr[i][j] = 0
  return count

COUNT = len(vacant)
maxi = 0

for i in range(COUNT - 2):
  for j in range(i + 1, COUNT - 1):
    for k in range(j + 1, COUNT):
      maxi = max(maxi, bfs([vacant[i], vacant[j], vacant[k]]))

print(maxi)