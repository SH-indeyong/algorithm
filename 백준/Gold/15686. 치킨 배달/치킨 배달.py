N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
home = []
chicken = []

# 집, 치킨집 위치 저장
for i in range(N):
  for j in range(N):
    if arr[i][j] == 1:
      home.append((i, j))
    elif arr[i][j] == 2:
      chicken.append((i, j))

def chicken_distance(lst):
  d = 0
  for hi, hj in home:
    m = 2 * N
    for  ci, cj in lst:
      m = min(abs(hi - ci) + abs(hj - cj), m)
    d += m
  return d

def dfs(n, lst):
  global mini
  # 종료 조건: 모든 치킨집의 폐업 여부 탐색 완료
  if n == len(chicken):
    if len(lst) == M:
      mini = min(chicken_distance(lst), mini)
    return
  
  # 유지하는 경우
  dfs(n + 1, lst + [chicken[n]])
  # 폐업하는 경우
  dfs(n + 1, lst)

# 최대 2N개의 집에서 나올 수 있는 최대 도시의 치킨 거리
mini = 2 * N * 2 * N
dfs(0, [])
print(mini)