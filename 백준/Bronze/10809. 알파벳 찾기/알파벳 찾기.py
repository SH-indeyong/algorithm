s = input()
alpha = [-1] * 26

for i in range(26):
  if chr(i+97) in s:
    alpha[i] = s.index(chr(i+97))
  print(alpha[i], end=' ')