a, b, c = int(input()), int(input()), int(input())

n = str(a * b * c)
counts = [0] * 10

for i in n:
  counts[int(i)] += 1

for j in range(10):
  print(counts[j])