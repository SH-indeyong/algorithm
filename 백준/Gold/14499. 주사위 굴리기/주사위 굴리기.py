N, M, ci, cj, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
move = list(map(int, input().split()))

#위  북  동  서  남  바닥
n1, n2, n3, n4, n5, n6 = 0, 0, 0, 0, 0, 0
# 동 서 북 남
di = [0, 0, 0, -1, 1]
dj = [0, 1, -1, 0, 0]

top = []

for dr in move:
  ni, nj = ci + di[dr], cj + dj[dr]

  # 범위 내에서만 실행
  if ni >= 0 and ni < N and nj >= 0 and nj < M:
    # 주사위 숫자 변경
    if dr == 1:
      n1, n3, n4, n6 = n4, n1, n6, n3
    elif dr == 2:
      n1, n3, n4, n6 = n3, n6, n1, n4
    elif dr == 3:
      n1, n2, n5, n6 = n5, n1, n6, n2
    else:
      n1, n2, n5, n6 = n2, n6, n1, n5

    # 지도의 숫자가 0인지 여부 따라 실행
    if arr[ni][nj] == 0:
      arr[ni][nj] = n6
    else:
      n6 = arr[ni][nj]
      arr[ni][nj] = 0
    
    top.append(n1)
    ci, cj = ni, nj

for i in top:
  print(i)