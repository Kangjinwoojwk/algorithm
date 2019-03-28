from queue import PriorityQueue
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for tc in range(1, int(input()) + 1):
    N = int(input())
    data = [list(map(int, input().split()))for _ in range(N)]
    visit = [[True] * N for _ in range(N)]
    d = [[2147483648] * N for _ in range(N)]
    Q = PriorityQueue()
    Q.put((0, 0, 0))
    d[0][0] = 0
    while visit[N - 1][N - 1]:
        w, x, y = Q.get()
        visit[x][y] = False
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if visit[nx][ny] and data[nx][ny] > data[x][y]:
                    if d[nx][ny] > d[x][y] + (data[nx][ny] - data[x][y]) + 1:
                        d[nx][ny] = d[x][y] + (data[nx][ny] - data[x][y]) + 1
                        Q.put((d[nx][ny], nx, ny))
                elif visit[nx][ny] and data[nx][ny] <= data[x][y]:
                    if d[nx][ny] > d[x][y] + 1:
                        d[nx][ny] = d[x][y] + 1
                        Q.put((d[nx][ny], nx, ny))
    print('#{} {}'.format(tc, d[N - 1][N - 1]))