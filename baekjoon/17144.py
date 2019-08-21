dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def spread():
    global data
    temp = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if data[i][j] > 0:
                for k in range(4):
                    x, y = i + dx[k], j + dy[k]
                    if 0 <= x < R and 0 <= y < C and data[x][y] != -1:
                        temp[x][y] += data[i][j] // 5
                    else:
                        temp[i][j] += data[i][j] // 5
                temp[i][j] += data[i][j] - 4 * (data[i][j] // 5)
            elif data[i][j] == -1:
                temp[i][j] = -1
    data = temp

def air_fresh():
    for i in range(airfresher[0] - 1, 0, -1):
        data[i][0] = data[i - 1][0]
    for i in range(C - 1):
        data[0][i] = data[0][i + 1]
    for i in range(airfresher[0]):
        data[i][C - 1] = data[i + 1][C - 1]
    for i in range(C - 1, 1, -1):
        data[airfresher[0]][i] = data[airfresher[0]][i - 1]
    data[airfresher[0]][1] = 0
    for i in range(airfresher[1] + 1, R - 1):
        data[i][0] = data[i + 1][0]
    for i in range(C - 1):
        data[R - 1][i] = data[R - 1][i + 1]
    for i in range(R - 1, airfresher[1], -1):
        data[i][C - 1] = data[i - 1][C - 1]
    for i in range(C - 1, 1, -1):
        data[airfresher[1]][i] = data[airfresher[1]][i - 1]
    data[airfresher[1]][1] = 0

R, C, T = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(R)]
airfresher=[]
for air in range(R):
    if data[air][0] == -1:
        airfresher.append(air)
for _ in range(T):
    spread()
    air_fresh()
print(2 + sum([sum(i) for i in data]))