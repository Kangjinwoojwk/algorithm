dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    data = [list(map(int, input().split())) for _ in range(h)]
    visit = [[True] * w for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if data[i][j] and visit[i][j]:
                ans += 1
                Q = [(i, j)]
                visit[i][j] = False
                while Q:
                    x, y = Q.pop()
                    for k in range(8):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < h and 0 <= ny < w and visit[nx][ny] and data[nx][ny]:
                            visit[nx][ny] = False
                            Q.append((nx, ny))
    print(ans)