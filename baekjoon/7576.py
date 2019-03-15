dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
from collections import deque
M, N = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
Q = deque()
ans = -1
for i in range(N):
    for j in range(M):
        if data[i][j] == 1:
            Q.append((i, j))
while Q:
    ans += 1
    for i in range(len(Q)):
        x, y = Q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if data[nx][ny] == 0:
                    data[nx][ny] = 1
                    Q.append((nx, ny))
for i in range(N):
    for j in range(M):
        if data[i][j] == 0:
            ans = -1
            break
print(ans)