s = input()
s = s.upper()
alpha = [0] * 26

for i in range(65, 91):
  c = chr(i)
  count = s.count(c)
  alpha[i - 65] = count

m = max(alpha)
if alpha.count(m) > 1:
  print('?')
else:
  print(chr(alpha.index(m) + 65))