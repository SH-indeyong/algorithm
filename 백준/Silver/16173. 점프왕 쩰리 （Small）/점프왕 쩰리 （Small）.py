n = int(input())

game_map = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

def dfs(col, row):
  if col < 0 or col >= n or row < 0 or row >= n:
    return False
  
  if game_map[col][row] == -1:
    return True
  
  if visited[col][row] == 0:
    visited[col][row] = 1
    jump = game_map[col][row]
    if jump == 0:
      return False
    return dfs(col + jump, row) or dfs(col, row + jump)
  return False

result = dfs(0, 0)
if result is True:
  print('HaruHaru')
else:
  print('Hing')