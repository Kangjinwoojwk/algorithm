dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y):
    global N, M
    data[x][y] = 3
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if data[nx][ny] == 0:
                dfs(nx, ny)


def cal():
    global N, M, ans
    for i in virus:
        for j in range(4):
            x, y = i[0] + dx[j], i[1] + dy[j]
            if 0 <= x < N and 0 <= y < M:
                if data[x][y] == 0:
                    dfs(x, y)
    cnt = 0
    for i in range(N):
        for j in range(M):
            if data[i][j] == 0:
                cnt += 1
            if data[i][j] == 3:
                data[i][j] = 0
    if cnt > ans:
        ans = cnt


def sol(x, y, wall):
    global N, M
    if wall == 0:
        cal()
        return
    if x == N:
        return
    if data[x][y] == 0:
        data[x][y] = 1
        if y == M - 1:
            sol(x + 1, 0, wall - 1)
        else:
            sol(x, y + 1, wall - 1)
        data[x][y] = 0
    if y == M - 1:
        sol(x + 1, 0, wall)
    else:
        sol(x, y + 1, wall)


N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
virus = []
for i in range(N):
    for j in range(M):
        if data[i][j] == 2:
            virus.append((i, j))
ans = 0
sol(0, 0, 3)
print(ans)