N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

pattern = [
  [(1, 0), (2, 0), (3, 0)], [(0, 1), (0, 2), (0, 3)],
  [((1, 0)), (1, 1), (0, 1)], 
  [(0, 1), (0, 2), (1, 2)], [(1, 0), (2, 0), (0, 1)], [(1, 0), (1, 1), (1, 2)], [(0, 1), (-1, 1), (-2, 1)],
  [(0, 1), (0, 2), (-1, 2)], [(-1, 0), (-2, 0), (0, 1)], [(-1, 0), (-1, 1), (-1, 2)], [(0, 1), (1, 1), (2, 1)],
  [(0, 1), (1, 1), (1, 2)], [(1, 0), (1, -1), (2, -1)], [(0, 1), (-1, 1), (-1, 2)], [(1, 0), (1, 1), (2, 1)], 
  [(1, 0), (2, 0), (1, 1)], [(1, 0), (2, 0), (1, -1)], [(0, 1), (0, 2), (1, 1)], [(0, 1), (0, 2), (-1, 1)]
]

result = 0
def cal(i, j, pos):
  n = arr[i][j]
  for di, dj in pos:
    ni, nj = i + di, j + dj
    if ni < 0 or ni >= N or nj < 0 or nj >= M:
      return 0
    else:
      n += arr[ni][nj]
  return n

for i in range(N):
  for j in range(M):
    for pos in pattern:
      s = cal(i, j, pos)
      result = max(s, result)

print(result)