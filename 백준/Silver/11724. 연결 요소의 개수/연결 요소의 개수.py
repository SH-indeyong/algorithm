import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n, m = map(int, input().split())

visited = [0] * (n + 1)
graph = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(m):
  u, v = map(int, input().split())
  graph[u][v] = 1
  graph[v][u] = 1

def dfs(vertex):
  if visited[vertex] == 0:
    visited[vertex] = 1
    for i in range(1, n + 1):
      if visited[i] == 0 and graph[vertex][i] == 1:
        dfs(i)

count = 0
for i in range(1, n + 1):
  if visited[i] == 0:
    dfs(i)
    count += 1

print(count)
