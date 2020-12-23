def sol(n, cnt):
    global ans
    if n >= N - 1:
        if cnt < ans:
            ans = cnt
        return
    if ans <= cnt:
        return
    for i in range(1, li[n] + 1):
        sol(n + i, cnt + 1)
T = int(input())
for tc in range(1, T + 1):
    li = list(map(int, input().split()))
    N = li[0]
    li = li[1:]
    ans = 100
    sol(0, -1)
    print('#{} {}'.format(tc, ans))