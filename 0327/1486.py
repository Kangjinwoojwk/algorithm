def sol(n, h):
    global ans, N
    if h >= B:
        if h < ans:
            ans = h
        return
    if n == N:
        return
    sol(n + 1, h)
    sol(n + 1, h + li[n])
T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    li = list(map(int, input().split()))
    li.sort(reverse=True)
    ans = 2**30
    sol(0, 0)
    print('#{} {}'.format(tc, ans - B))