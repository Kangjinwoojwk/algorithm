import sys
sys.stdin = open('1949.txt', 'r')
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def sol(x, y, cnt, can):
    global ans, N, K
    if cnt > ans:
        ans = cnt
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny]:
            if data[nx][ny] < data[x][y]:
                visited[nx][ny] = False
                sol(nx, ny, cnt + 1, can)
                visited[nx][ny] = True
            elif can and data[nx][ny] - data[x][y] < K:
                a = data[nx][ny]
                data[nx][ny] = data[x][y] - 1
                visited[nx][ny] = False
                sol(nx, ny, cnt + 1, False)
                visited[nx][ny] = True
                data[nx][ny] = a


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [[True] * N for _ in range(N)]
    start = []
    max_height = 0
    for i in range(N):
        for j in range(N):
            if data[i][j] > max_height:
                max_height = data[i][j]
    for i in range(N):
        for j in range(N):
            if data[i][j] == max_height:
                start.append([i, j])
    ans = 0
    start_cnt = len(start)
    for i in range(start_cnt):
        visited[start[i][0]][start[i][1]] = False
        sol(start[i][0], start[i][1], 1, True)
        visited[start[i][0]][start[i][1]] = True
    print('#{} {}'.format(tc, ans))