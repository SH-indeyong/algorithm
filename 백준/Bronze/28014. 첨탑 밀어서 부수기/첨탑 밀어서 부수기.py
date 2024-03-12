import sys
input = sys.stdin.readline

n = int(input())
h = list(map(int, input().split()))
m = 0
count = 0

for i in range(n):
  a = h[i]
  if a >= m:
    count += 1
  m = a

print(count)