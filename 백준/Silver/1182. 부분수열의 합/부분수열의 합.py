N, S = map(int, input().split())
arr = list(map(int, input().split()))
num = 0

def cal(idx, sum):
    global num

    if idx == N:
        return

    sum += arr[idx]

    if sum == S:
        num += 1
    
    # arr[idx]를 선택한 경우의 가지
    cal(idx + 1, sum)
    # arr[idx]를 선택하지 않은 경우의 가지
    cal(idx + 1, sum - arr[idx])

cal(0, 0)
print(num)