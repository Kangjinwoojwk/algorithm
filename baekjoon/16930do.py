from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
N, M, K = map(int, input().split())
data = [list(input()) for _ in range(N)]
visit = [[0]*M for _ in range(N)]
x1, y1, x2, y2 = map(int, input().split())
x1 -= 1
x2 -= 1
y1 -= 1
y2 -= 1
queue = deque()
queue.append((x1, y1))
while visit[x2][y2] == 0:
    if not queue:
        break
    x, y = queue.popleft()
    for i in range(4):
        for j in range(1, K + 1):
            nx, ny = x + j * dx[i], y + j * dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                break
            elif visit[nx][ny]:
                pass
            elif data[nx][ny] == '#':
                break
            elif data[nx][ny] == '.':
                visit[nx][ny] = visit[x][y] + 1
                queue.append((nx, ny))
if visit[x2][y2] == 0:
    print(-1)
else:
    print(visit[x2][y2])