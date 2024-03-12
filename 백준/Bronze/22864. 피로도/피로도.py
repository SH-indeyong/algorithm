a, b, c, m = map(int, input().split())
work = 0
piro = 0
time = 0

while time < 24:
  # 증가하는 피로도가 최대 피로도를 초과하는 경우 일을 할 수 없음
  if a > m:
    break
  
  if piro <=m and piro + a <= m :
    work += b
    piro += a
  else:
    piro -= c
    if piro < 0:
      piro = 0
  time += 1

print(work)