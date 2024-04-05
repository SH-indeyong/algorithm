import sys
input = sys.stdin.readline

n = int(input())
student = list(map(int, input().split()))
b, c = map(int, input().split())
m = n

for i in student:
  i -= b
  if i > 0:
    m += i // c
    if i % c != 0:
      m += 1

print(m)