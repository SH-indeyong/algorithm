import sys
input = sys.stdin.readline

num = [int(input()) for i in range(9)]

maxi = max(num)
print(maxi)
print(num.index(maxi) + 1)