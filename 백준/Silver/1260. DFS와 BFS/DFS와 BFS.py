n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(start):
  print(start, end=' ')
  visited[start] = 1
  for connect in sorted(graph[start]):
    if visited[connect] == 0:
      dfs(connect)

def bfs(start):
  visited[start] = 1
  queue = [start]
  while queue:
    node = queue.pop(0)
    print(node, end=' ')
    for connect in sorted(graph[node]):
      if visited[connect] == 0:
        visited[connect] = 1
        queue.append(connect)

visited = [0] * (n + 1)
dfs(v)
print("")
visited = [0] * (n + 1)
bfs(v)