n = int(input())
p = list(map(int, input().split()))

high = 0
count = 0
result = 0

for i in p:
  if i > high:
    high = i
    count = 0
  else:
    count += 1
  result = max(result, count)

print(result)