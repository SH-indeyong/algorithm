import sys
input = sys.stdin.readline
s = 'A' + input()

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = 0

for i in range(len(s) - 2):
  time = abs(alpha.index(s[i]) - alpha.index(s[i + 1]))
  if time > 13:
    time = 26 - time
  result += time

print(result)