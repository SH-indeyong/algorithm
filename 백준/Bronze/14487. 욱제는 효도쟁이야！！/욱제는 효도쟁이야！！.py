n = int(input())
town = list(map(int, input().split()))
price = 0

i = 0
while i < n:
  price += town[i]
  i += 1

print(price - max(town))