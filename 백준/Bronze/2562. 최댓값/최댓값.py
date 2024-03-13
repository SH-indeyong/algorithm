import sys
input = sys.stdin.readline

num = []
for i in range(9):
  num.append(int(input()))

maxi = max(num)
print(maxi)
print(num.index(maxi) + 1)