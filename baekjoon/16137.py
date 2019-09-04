dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
move = [[[5000] * N for _ in range(N)] for __ in range(2)]
use = [[True] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if data[i][j] != 1:
            if (i - 1 >= 0 and data[i - 1][j] != 1) or (i + 1 < N and data[i + 1][j] != 1):
                if (j - 1 >= 0 and data[i][j - 1] != 1) or (j + 1 < N and data[i][j + 1] != 1):
                    use[i][j] = False
queue = [(0, 0, 0)]
move[0][0][0] = 0
while move[0][N - 1][N - 1] == 5000 and move[1][N - 1][N - 1] == 5000:
    x, y, pan = queue.pop(0)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if data[nx][ny] == 1:
                if move[pan][nx][ny] >= 5000:
                    move[pan][nx][ny] = move[pan][x][y] + 1
                    queue.append((nx, ny, pan))
            elif data[nx][ny] > 1:
                if move[pan][nx][ny] >= 5000:
                    move[pan][nx][ny] = ((move[pan][x][y] // data[nx][ny]) + 1) * data[nx][ny]
                    queue.append((nx, ny, pan))
            else:
                if pan == 0 and use[nx][ny]:
                    if move[pan + 1][nx][ny] >= 5000:
                        move[pan + 1][nx][ny] = ((move[pan][x][y] // M) + 1) * M
                        queue.append((nx, ny, pan + 1))
print(min(move[0][N - 1][N - 1], move[1][N - 1][N - 1]))