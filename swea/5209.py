def sol(n, price):
    global ans, N
    if ans <= price:
        return
    if n == N:
        ans = price
    for i in range(N):
        if visit[i]:
            visit[i] = False
            sol(n + 1, price + data[n][i])
            visit[i] = True
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    visit = [True] * N
    ans = 2 ** 30
    sol(0, 0)
    print('#{} {}'.format(tc, ans))