import sys
input = sys.stdin.readline

input()
num = list(map(int, input().split()))
print(min(num), max(num))