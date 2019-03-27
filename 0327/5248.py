def sol(n):
    visit[n] = False
    for i in edge[n]:
        if visit[i]:
            sol(i)
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    li = list(map(int, input().split()))
    edge = [[] for _ in range(N + 1)]
    for i in range(M):
        edge[li[2 * i]].append(li[2 * i + 1])
        edge[li[2 * i + 1]].append(li[2 * i])
    visit = [True] * (N + 1)
    ans = 0
    for i in range(1, N + 1):
        if visit[i]:
            sol(i)
            ans += 1
    print('#{} {}'.format(tc, ans))
