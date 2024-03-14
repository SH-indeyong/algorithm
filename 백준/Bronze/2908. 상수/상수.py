a, b = input().split()
aa = int(a[2]) * 100 + int(a[1]) * 10 + int(a[0])
bb = int(b[2]) * 100 + int(b[1]) * 10 + int(b[0])

print(max(aa, bb))