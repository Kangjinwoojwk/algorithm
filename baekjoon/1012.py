dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y):
    global N, M
    st = [(x, y)]
    while st:
        for i in range(len(st)):
            x, y = st.pop()
            for j in range(4):
                nx, ny = x + dx[j], y + dy[j]
                if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] and data[nx][ny]:
                    visit[nx][ny] = False
                    st.append((nx, ny))


T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())
    data = [[0] * M for _ in range(N)]
    visit = [[True] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        data[y][x] = 1
    ans = 0
    for i in range(N):
        for j in range(M):
            if data[i][j] == 1 and visit[i][j]:
                visit[i][j] = False
                dfs(i, j)
                ans += 1
    print(ans)