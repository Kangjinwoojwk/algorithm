dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
arr = [0, 0, 0, 0]
ans = 0
def sol(x, y, n):
    global ans
    if n == 4:
        if sum(arr) > ans:
            ans = sum(arr)
        return
    arr[n] = data[x][y]
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = True
            sol(nx, ny, n + 1)
            visited[nx][ny] = False
def sol1(x, y):
    global ans, arr
    for k in range(4):
        arr = [data[x][y]]
        for l in range(4):
            if k == l:
                continue
            if not (0 <= x + dx[l]< N and 0 <= y + dy[l] < M):
                break
            arr.append(data[x + dx[l]][y + dy[l]])
        if sum(arr) > ans:
            ans = sum(arr)
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        sol(i, j, 0)
        visited[i][j] = False
for i in range(N):
    for j in range(M):
        sol1(i, j)
print(ans)