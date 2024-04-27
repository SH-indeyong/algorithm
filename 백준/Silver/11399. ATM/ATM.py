n = int(input())
arr = list(map(int, input().split()))
arr.sort()
sum = 0
total = [0] * n
for i in range(n):
    sum += arr[i]
    total[i] = sum

result = 0
for i in total:
    result += i

print(result)