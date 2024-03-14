T = int(input())

for t in range(T):
  s = input()
  score, total = 0, 0

  for i in s:
    if i == 'O':
      score += 1
    else:
      score = 0
    total += score

  print(total)