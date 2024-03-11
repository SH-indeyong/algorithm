n = int(input())
store = list(map(int, input().split()))
milk = [0, 1, 2] * (int(n/3) + 1)
count = 0

for i in range(n):
  if store[i] == milk[count]:
    count += 1
  else: continue

print(count)