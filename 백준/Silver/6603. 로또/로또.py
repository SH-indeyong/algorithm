def pick_lotto(lotto, arr, index, count):
    if count == 6:
        print(*lotto)
        # print(' '.join(map(str, lotto)))
        return

    for i in range(index, arr[0]):
        lotto[count] = arr[i + 1]
        pick_lotto(lotto, arr, i + 1, count + 1)

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break

    lotto = [0] * 6
    pick_lotto(lotto, arr, 0, 0)
    print()
