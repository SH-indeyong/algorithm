import sys
sys.setrecursionlimit(10000)

t = int(input())

for i in range(t):
  m, n, k = map(int, input().split())
  worm = 0

  bechu = [[0] * m for _ in range(n)]
  for j in range(k):
    row, col = map(int, input().split())
    bechu[col][row] = 1

  def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
      return False
    
    if bechu[x][y] == 1:
      bechu[x][y] = 0
      dfs(x + 1, y)
      dfs(x - 1, y)
      dfs(x, y + 1)
      dfs(x, y - 1)
      return True
    return False
      
  for l in range(m):
    for k in range(n):
      if dfs(k, l) == True:
        worm += 1

  print(worm)