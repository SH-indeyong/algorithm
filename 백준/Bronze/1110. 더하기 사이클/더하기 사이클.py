num = int(input())
if num == 0:
  print(1)
  exit()

a = int(num/10)
b = int(num%10)
new = 0
count = 0

while new != num:
  new = b * 10 + (a + b) % 10
  a = int(new/10)
  b = int(new%10)
  count += 1

print(count)