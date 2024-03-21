import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
max_high = 100
min_high = 1
count_list = [1]

graph = [[0] * n for _ in range(n)]
for i in range(n):
  graph[i] = list(map(int, input().split()))
  # 최고 높이, 최소 높이 갱신
  min_high = min(min_high, min(graph[i]))
  max_high = max(max_high, max(graph[i]))

def bfs(x, y, rain, visited):
  queue = deque()
  visited[x][y] = 1
  queue.append((x, y))
  dx = [0, 0, -1, 1]
  dy = [-1, 1, 0, 0]

  while queue:
    before_x, before_y = queue.popleft()
    for i in range(4):
      next_x = before_x + dx[i]
      next_y = before_y + dy[i]
      if 0 <= next_x < n and 0 <= next_y < n and not visited[next_x][next_y] and graph[next_x][next_y] > rain:
        visited[next_x][next_y] = 1
        queue.append((next_x, next_y))

for rain in range(min_high, max_high):
  count = 0
  visited = [[0] * n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if graph[i][j] > rain and visited[i][j] == 0:
        bfs(i, j, rain, visited)
        count += 1
  count_list.append(count)

print(max(count_list))