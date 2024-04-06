N, M = map(int, input().split())
start_i, start_j, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
count = 0

#     북 동 남 서
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def clean(current_i, current_j, d):
  global count
  while 1:
    # 방문완료 표시
    arr[current_i][current_j] = 2
    count += 1

    # 왼쪽 방향으로 탐색하여 미청소 영역인 경우 이동
    flag = 1
    while flag == 1:
      for next_d in ((d + 3) % 4, (d + 2) % 4, (d + 1) % 4, d):
        next_i, next_j = current_i + di[next_d], current_j + dj[next_d]
        if arr[next_i][next_j] == 0:
          current_i, current_j, d = next_i, next_j, next_d
          flag = 0
          break
      # 4방향 모두 청소 완료 ---> 후진
      else:
        back_i, back_j = current_i - di[d], current_j - dj[d]
        if arr[back_i][back_j] == 1:
          return
        else:
          current_i, current_j = back_i, back_j

clean(start_i, start_j, d)

print(count)