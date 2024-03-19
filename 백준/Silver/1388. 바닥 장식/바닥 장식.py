n, m = map(int, input().split())
result = 0

floor = []
for i in range(n):
  floor.append(list(input()))

def dfs_width(x, y):
  if x < 0 or x >= n or y < 0 or y >= m:
    return False
  
  if floor[x][y] == '-':
    floor[x][y] = 0
    dfs_width(x, y + 1)
    dfs_width(x, y - 1)
    return True
  return False

def dfs_height(x, y):
  if x < 0 or x >= n or y < 0 or y >= m:
    return False
  
  if floor[x][y] == '|':
    floor[x][y] = 0
    dfs_height(x + 1, y)
    dfs_height(x - 1, y)
    return True
  return False

for i in range(n):
  for j in range(m):
    if floor[i][j] == '-':
      if dfs_width(i, j) == True:
        result += 1
    elif floor[i][j] == '|':
      if dfs_height(i, j) == True:
        result += 1

print(result)