arr = input().split('-')
cal = []

for i in arr:
    sum = 0
    num = i.split('+')
    for j in num:
        sum += int(j)
    cal.append(sum)

answer = cal[0]

for i in range(1, len(cal)):
    answer -= cal[i]
print(answer)