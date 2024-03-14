T = int(input())

for i in range(T):
  p = ''
  r, s = input().split()
  
  for j in range(len(s)):
    p += s[j] * int(r)
  print(p)