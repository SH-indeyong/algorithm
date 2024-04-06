N = 4
arr = [list(map(int, str(input()))) for _ in range(N)]
k = int(input())
top = [0] * N

for _ in range(k):
  w, d = map(int, input().split())
  w -= 1

  # w 톱니 회전
  rot_list = [(w, 0)]

  # 오른쪽 톱니 회전
  for i in range(w + 1, N):
    if arr[i - 1][(top[i - 1] + 2) % 8] != arr[i][(top[i] + 6) % 8]:
      rot_list.append((i, (i - w) % 2))
    else:
        break

  # 왼쪽 톱니 회전
  for i in range(w - 1, -1, -1):
    if arr[i][(top[i] + 2) % 8] != arr[i + 1][(top[i + 1] + 6) % 8]:
      rot_list.append((i, (w - i) % 2))
    else:
        break
    
  # 회전
  for i, rotate in rot_list:
    # w 톱니와 같은 방향
    if rotate == 0:
      top[i] = (top[i] - d + 8) % 8
    else:
      top[i] = (top[i] + d + 8) % 8

result = 0
table = [1, 2, 4, 8]
for i in range(N):
  result += arr[i][top[i]] * table[i]
print(result)