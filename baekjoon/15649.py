def sol(m):
    global N, M
    if m == M:
        print(' '.join(map(str, result)))
        return
    for i in range(N):
        if visit[i]:
            visit[i] = False
            result[m] = i + 1
            sol(m + 1)
            visit[i] = True


N, M = map(int, input().split())
visit = [True] * N
result = [0] * M
sol(0)