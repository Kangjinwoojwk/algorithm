dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
R, C, M = map(int, input().split())
data = [[[0] * 3 for __ in range(C)] for _ in range(R)]
answer = 0
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    data[r - 1][c - 1] = [s, d - 1, z]


def move():
    global data
    temp_data = [[[0] * 3 for __ in range(C)] for _ in range(R)]
    for x in range(C):
        for y in range(R):
            if data[y][x][2] == 0:
                continue
            nx = (x + (dx[data[y][x][1]] * data[y][x][0])) % (2 * (C - 1))
            ny = (y + (dy[data[y][x][1]] * data[y][x][0])) % (2 * (R - 1))
            if nx > C - 1:
                nx = C - 1 - (nx - (C - 1))
                if data[y][x][1] == 2:
                    data[y][x][1] = 3
                else:
                    data[y][x][1] = 2
            if ny > R - 1:
                ny = R - 1 - (ny - (R - 1))
                if data[y][x][1] == 0:
                    data[y][x][1] = 1
                else:
                    data[y][x][1] = 0
            if temp_data[ny][nx][2] < data[y][x][2]:
                temp_data[ny][nx] = data[y][x][:]
            else:
                continue
    data = temp_data


for i in range(C):
    for j in range(R):
        if data[j][i][2] != 0:
            answer += data[j][i][2]
            data[j][i] = [0, 0, 0]
            break
    move()
print(answer)