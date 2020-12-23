def click(x, y):
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if data[nx][ny] == '*':
                data[x][y] = '0'
                return
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if data[nx][ny] == '.':
                data[nx][ny] = '0'
                click(nx, ny)


dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
for tc in range(1, int(input()) + 1):
    N = int(input())
    data = [list(input()) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            if data[i][j] == '.':
                for k in range(8):
                    cx, cy = i + dx[k], j + dy[k]
                    if 0 <= cx < N and 0 <= cy < N:
                        if data[cx][cy] == '*':
                            break
                else:
                    data[i][j] = '0'
                    click(i, j)
                    ans += 1
    for i in range(N):
        for j in range(N):
            if data[i][j] == '.':
                ans += 1
    print('#{} {}'.format(tc, ans))