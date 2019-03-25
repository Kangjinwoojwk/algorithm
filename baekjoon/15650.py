def sol(n, ptr):
    global N, M
    if n == M:
        print(' '.join(map(str, result)))
        return
    for i in range(ptr, N):
        if visit[i]:
            visit[i] = False
            result[n] = i + 1
            sol(n + 1, i + 1)
            visit[i] = True

N, M = map(int, input().split())
result = [0] * M
visit = [True] * N
sol(0, 0)