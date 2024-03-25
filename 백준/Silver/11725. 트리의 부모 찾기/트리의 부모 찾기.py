import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
visited = [False] * (n + 1)
nodes = [[] for _ in range(n + 1)]
answer = [0] * (n + 1)

for i in range(n - 1):
  a, b = map(int, input().split())
  nodes[a].append(b)
  nodes[b].append(a)

def bfs(nodes, node, visited):
  que = deque([node])
  visited[node] = True
  while que:
    x = que.popleft()
    for i in nodes[x]:
      if not visited[i]:
        answer[i] = x
        que.append(i)
        visited[i] = True

bfs(nodes, 1, visited)

for i in range(2, n + 1):
  print(answer[i])