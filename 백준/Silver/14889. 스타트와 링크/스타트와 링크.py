N = int(input())
M = N // 2
arr = [list(map(int, input().split())) for _ in range(N)]
# 능력치의 최댓값이 100이므로 result의 충분한 최댓값은 100 * M * M
result = 100 * M * M

def diff(start, link):
  start_power, link_power = 0, 0
  for i in range(M):
    for j in range(M):
      start_power += arr[start[i]][start[j]]
      link_power += arr[link[i]][link[j]]
  return abs(start_power - link_power)

def dfs(n, start, link):
  global result
  # start팀과 link팀이 같은 인원수가 되었을 경우
  if n == N:
    if len(start) == len(link):
      result = min(result, diff(start, link))
    return
  
  # start팀을 선택하는 경우
  dfs(n + 1, start + [n], link)
  # link팀을 선택하는 경우
  dfs(n + 1, start, link + [n])

dfs(0, [], [])

print(result)