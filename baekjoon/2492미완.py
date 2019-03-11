N, M, T, K = map(int, input().split())
dia_map = [[0] * (N + 1) for _ in range(M + 1)]
for i in range(T):
    y, x = map(int, input().split())
    dia_map[x][y] = 1
max_v = 0
X, Y = 0, 0
for i in range(N + 1 - K):
    for j in range(M + 1 - K):
        sumv = 0
        for k in range(K + 1):
            for l in range(K + 1):
                sumv += dia_map[j+l][i+k]
        if max_v < sumv:
            max_v = sumv
            X, Y = j, i + K
print(X, Y)
print(max_v)