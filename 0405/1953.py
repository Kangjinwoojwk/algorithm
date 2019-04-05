dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
for tc in range(1, int(input()) + 1):
    N, M, R, C, L = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    visit = [[True] * M for i in range(N)]
    ans = 0
    Q = [(R, C)]
    visit[R][C] = False
    ans += 1
    L -= 1
    while L:
        L -= 1
        for i in range(len(Q)):
            x, y = Q.pop(0)
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < M:
                    if i == 0:
                        if data[x][y] == 1 or data[x][y] == 3 or data[x][y] == 6 or data[x][y] == 7:
                            if data[nx][ny] == 1 or data[nx][ny] == 3 or data[nx][ny] == 4 or data[nx][ny] == 5:
                                if visit[nx][ny]:
                                    visit[nx][ny] = False
                                    ans += 1
                                    Q.append((nx, ny))
                    if i == 1:
                        if data[x][y] == 1 or data[x][y] == 3 or data[x][y] == 4 or data[x][y] == 5:
                            if data[nx][ny] == 1 or data[nx][ny] == 3 or data[nx][ny] == 6 or data[nx][ny] == 7:
                                if visit[nx][ny]:
                                    visit[nx][ny] = False
                                    ans += 1
                                    Q.append((nx, ny))
                    if i == 2:
                        if data[x][y] == 1 or data[x][y] == 2 or data[x][y] == 5 or data[x][y] == 6:
                            if data[nx][ny] == 1 or data[nx][ny] == 2 or data[nx][ny] == 4 or data[nx][ny] == 7:
                                if visit[nx][ny]:
                                    visit[nx][ny] = False
                                    ans += 1
                                    Q.append((nx, ny))
                    if i == 3:
                        if data[x][y] == 1 or data[x][y] == 2 or data[x][y] == 4 or data[x][y] == 7:
                            if data[nx][ny] == 1 or data[nx][ny] == 2 or data[nx][ny] == 5 or data[nx][ny] == 6:
                                if visit[nx][ny]:
                                    visit[nx][ny] = False
                                    ans += 1
                                    Q.append((nx, ny))
    print('#%d %d'%(tc, ans))

