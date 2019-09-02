dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
N, M = map(int, input().split())
r, c, d = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
visited = [[True] * M for _ in range(N)]
robot = [r, c]
x, y = robot
while True:
    visited[x][y] = False
    temp_d = d
    for i in range(4):
        temp_d = (temp_d - 1) % 4
        if data[x + dx[temp_d]][y + dy[temp_d]] or not visited[x + dx[temp_d]][y + dy[temp_d]]:
            continue
        else:
            x, y = x + dx[temp_d], y + dy[temp_d]
            d = temp_d
            break
    else:
        if data[x - dx[d]][y - dy[d]]:
            break
        x, y = x - dx[d], y - dy[d]
ans = sum([i.count(False) for i in visited])
print(ans)