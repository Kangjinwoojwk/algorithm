dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
N, M = map(int, input().split())
data = [input() for _ in range(N)]
visit = [[True] * M for _ in range(N)]
Q = [(0, 0)]
visit[0][0] = False
ans = 1
while visit[N - 1][M - 1]:
    for _ in range(len(Q)):
        x, y = Q.pop(0)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if visit[nx][ny] and data[nx][ny] == '1':
                    visit[nx][ny] = False
                    Q.append((nx, ny))
    ans += 1
print(ans)