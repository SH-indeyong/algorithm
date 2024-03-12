n, l, k = map(int, input().split())
score = 0
quest = []

for i in range(n):
  sub1, sub2 = map(int, input().split())
  if sub2 <= l:
    quest.append(140)
  elif sub1 <= l:
    quest.append(100)
  else:
    quest.append(0)

quest.sort(reverse=True)
for i in range(k):
  score += quest[i]

print(score)
