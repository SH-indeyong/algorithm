s = input()
alpha = [0] * 26

for i in s:
  o = ord(i)
  if o > 96:
    o -= 32
  alpha[o - 65] += 1

if alpha.count(max(alpha)) > 1:
  print('?')
else:
  print(chr(alpha.index(max(alpha)) + 65))