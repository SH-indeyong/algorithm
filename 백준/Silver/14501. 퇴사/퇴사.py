N = int(input())
T = [0] * N
P = [0] * N

for i in range(N):
  T[i], P[i] = map(int, input().split())

def dfs(n, s):
  global result

  # 종료조건: n을 종료에 관련된 것으로 정의
  if n >= N:
    result = max(result, s)
    return
  
  # 상담하는 경우
  if n + T[n] <= N:
    dfs(n + T[n], s + P[n])

  # 상담하지 않는 경우
  dfs(n + 1, s)

result = 0
# dfs(날짜, 수익)
dfs(0, 0)

print(result)