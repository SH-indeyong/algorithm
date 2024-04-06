N = int(input())
A = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
mini = 1000000000
maxi = -1000000000

def dfs(n, now, add, sub, mul, div):
  global mini, maxi

  # 종료조건
  if n == N:
    mini = min(mini, now)
    maxi = max(maxi, now)
    return
  
  if add > 0:
    dfs(n + 1, now + A[n], add - 1, sub, mul, div)
  if sub > 0:
    dfs(n + 1, now - A[n], add, sub - 1, mul, div)
  if mul > 0:
    dfs(n + 1, now * A[n], add, sub, mul - 1, div)
  if div > 0:
    dfs(n + 1, int(now / A[n]), add, sub, mul, div - 1)

dfs(1, A[0], add, sub, mul, div)

print(maxi, mini)