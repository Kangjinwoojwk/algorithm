dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    global area, N, M
    st = [(x, y)]
    while st:
        for i in range(len(st)):
            x, y = st.pop()
            ans[area] += 1
            for j in range(4):
                nx, ny = x + dx[j], y + dy[j]
                if 0 <= nx < M and 0 <= ny < N and data[nx][ny]:
                    data[nx][ny] = False
                    st.append((nx, ny))



M, N, K = map(int, input().split())
data = [[True] * N for _ in range(M)]
ans = []
area = 0
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            data[j][i] = False
for i in range(M):
    for j in range(N):
        if data[i][j]:
            data[i][j] = False
            ans.append(0)
            dfs(i, j)
            area += 1
ans.sort()
print(area)
print(' '.join(map(str, ans)))