def binary_Search(n, start, end, dir):
    global ans
    if start > end:
        return
    pivot = (start + end) // 2
    if binary[pivot] == n:
        ans += 1
        return
    elif binary[pivot] > n:
        if dir != -1:
            binary_Search(n, start, pivot - 1, -1)
    elif binary[pivot] < n:
        if dir != 1:
            binary_Search(n, pivot + 1, end, 1)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    binary = list(map(int, input().split()))
    binary.sort()
    li = list(map(int, input().split()))
    ans = 0
    for i in li:
        binary_Search(i, 0, N - 1, 0)
    print('#{} {}'.format(tc, ans))