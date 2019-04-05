dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]
def dead():
    for i in range(N):
        data[0][i][0] //= 2
        data[0][i][1] = 2
        data[N - 1][i][0] //= 2
        data[N - 1][i][1] = 1
        data[i][0][0] //= 2
        data[i][0][1] = 4
        data[i][N - 1][0] //= 2
        data[i][N - 1][1] = 3

def move():
    global data
    temp = [[[0] * 2 for _ in range(N)] for __ in range(N)]
    meet = dict()
    for i in range(N):
        for j in range(N):
            if data[i][j][0]:
                x, y = i + dx[data[i][j][1]], j + dy[data[i][j][1]]
                if temp[x][y][0]:
                    if (x, y) not in meet:
                        meet[(x, y)] = [data[i][j][:]]
                        meet[(x, y)].append(temp[x][y][:])
                    else:
                        meet[(x, y)].append(data[i][j][:])
                temp[x][y][0] += data[i][j][0]
                temp[x][y][1] += data[i][j][0]
    for k, v in meet.items():
        x, y = k
        temp[x][y][1] = max(v)[1]
    data = temp
    dead()


for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    data = [[[0] * 2 for _ in range(N)] for __ in range(N)]
    for i in range(K):
        x, y, micro, direction = map(int, input().split())
        data[x][y][0] = micro
        data[x][y][1] = direction
    for i in range(M):
        move()
    ans = 0
    for i in range(N):
        for j in range(N):
            ans += data[i][j][0]
    print('#%d %d'%(tc, ans))