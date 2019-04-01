def sol(n):
    if n == N:
        print(' '.join(result))
        return
    for i in range(N):
        if visit[i]:
            visit[i] = False
            result[n] = str(i + 1)
            sol(n + 1)
            visit[i] = True
N = int(input())
visit = [True] * N
result = [''] * N
sol(0)