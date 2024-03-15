T = int(input())

for t in range(T):
  h, w, n = map(int, input().split())
  x, y = 1, 1
  
  for i in range(n-1):
    x += 1
    if x > h:
      x = 1
      y += 1

  if len(str(y)) < 2:
    print(str(x) + '0' + str(y))
  else:
    print(str(x) + str(y))