num = int(input())
a = num//10
b = num%10
count = 0

while True:
  new = b * 10 + (a + b) % 10
  a = new//10
  b = new%10
  count += 1
  if num == new: 
    break
  else: 
    continue

print(count)