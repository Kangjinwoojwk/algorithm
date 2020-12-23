T = int(input())
def sol(now, power):
    global N, ans
    if power > ans:
        return
    if True not in visit:
        if power + data[now][0] < ans:
            ans = power + data[now][0]
        return
    for i in range(N):
        if visit[i]:
            visit[i] = False
            sol(i, power + data[now][i])
            visit[i] = True
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    ans = 2**30
    visit = [True] * N
    visit[0] = False
    sol(0, 0)
    print('#{} {}'.format(tc, ans))