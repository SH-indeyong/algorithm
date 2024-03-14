n = int(input())
f = [0] * (n+1)
if n == 0:
  print(0)
  exit()
f[1] = 1

for i in range(2, n+1):
  f[i] = f[i-2] + f[i-1]

print(f[n])