def sol(n, cnt):
    if cnt == 6:
        print(' '.join(map(str, result)))
        return
    if n == N:
        return
    result[cnt] = li[n]
    sol(n + 1, cnt + 1)
    sol(n + 1, cnt)
while True:
    li = list(map(int, input().split()))
    if li[0] == 0:
        exit()
    N = li.pop(0)
    li.sort()
    result = [0] * 6
    sol(0, 0)
    print()