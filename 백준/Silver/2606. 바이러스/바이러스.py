node = int(input())
edge = int(input())

graph = [[] for i in range(node + 1)]
visited = [0] * (node  + 1)

for i in range(edge):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(com):
  visited[com] = 1
  for connect in graph[com]:
    if visited[connect] == 0:
      dfs(connect)

dfs(1)

print(sum(visited) - 1)