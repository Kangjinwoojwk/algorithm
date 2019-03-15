dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, n):
    global N
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N :
                if data[nx][ny] > n and visit[nx][ny]:
                    visit[nx][ny] = False
                    stack.append((nx, ny))

def sol(n):
    global N, ans
    area = 0
    for i in range(N):
        for j in range(N):
            if data[i][j] > n and visit[i][j]:
                visit[i][j] = False
                dfs(i, j, n)
                area += 1
    if area > ans:
        ans = area


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
max_height = 0
ans = 0
for i in range(N):
    for j in range(N):
        if data[i][j] > max_height:
            max_height = data[i][j]
for i in range(max_height):
    visit = [[True] * N for _ in range(N)]
    sol(i)
print(ans)