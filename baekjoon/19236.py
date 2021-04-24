dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
data = [[[[0, 0] for _ in range(4)] for __ in range(4)] for ___ in range(16)]
for _ in range(4):
    a0, b0, a1, b1, a2, b2, a3, b3 = map(int, input().split())
    data[0][_][0] = [a0, b0 - 1]
    data[0][_][1] = [a1, b1 - 1]
    data[0][_][2] = [a2, b2 - 1]
    data[0][_][3] = [a3, b3 - 1]
answer = 0


def move(x, y, n):
    for fish_num in range(1, 17):
        for i in range(4):
            for j in range(4):
                if fish_num == data[n][i][j][0]:
                    temp = 0
                    while i + dx[data[n][i][j][1]] < 0 or i + dx[data[n][i][j][1]] > 3 \
                            or j + dy[data[n][i][j][1]] < 0 or j + dy[data[n][i][j][1]] > 3 \
                            or (x == i + dx[data[n][i][j][1]] and y == j + dy[data[n][i][j][1]]):
                        data[n][i][j][1] = (data[n][i][j][1] + 1) % 8
                        temp += 1
                        if temp == 8:
                            break
                    else:
                        data[n][i + dx[data[n][i][j][1]]][j + dy[data[n][i][j][1]]], data[n][i][j] = \
                            data[n][i][j], data[n][i + dx[data[n][i][j][1]]][j + dy[data[n][i][j][1]]]
                    fish_num = 17


def sol(x, y, eaten, cnt):
    global answer
    for i in range(4):
        for j in range(4):
            data[cnt][i][j] = data[cnt - 1][i][j][:]
    eaten += data[cnt][x][y][0]
    if eaten > answer:
        answer = eaten
    data[cnt][x][y][0] = 0
    move(x, y, cnt)
    for i in range(4):
        if 0 <= x + i * dx[data[cnt][x][y][1]] < 4 and 0 <= y + i * dy[data[cnt][x][y][1]] < 4 and\
                data[cnt][x + i * dx[data[cnt][x][y][1]]][y + i * dy[data[cnt][x][y][1]]][0]:
            sol(x + i * dx[data[cnt][x][y][1]], y + i * dy[data[cnt][x][y][1]], eaten, cnt + 1)


sol(0, 0, 0, 1)
print(answer)