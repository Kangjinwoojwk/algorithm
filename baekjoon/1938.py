dx = [-1, 1, 0, 0, 0]
dy = [0, 0, -1, 1, 0]
ds = [0, 0, 0, 0, 1]
N = int(input())
data = [list(input()) for _ in range(N)]
state = set()
queue = list()
end = tuple()
ans = 0
check_end = False
for i in range(N):
    for j in range(N):
        if data[i][j] == 'B' and not state:
            if i + 1 < N and data[i + 1][j] == 'B':
                state.add((i + 1, j, 1))
                queue.append((i + 1, j, 1))
                data[i + 1][j] = data[i + 2][j] = data[i][j] = '0'
            elif j + 1 < N and data[i][j + 1] == 'B':
                state.add((i, j + 1, 0))
                queue.append((i, j + 1, 0))
                data[i][j + 1] = data[i][j + 2] = data[i][j] = '0'
        if data[i][j] == 'E' and not end:
            if i + 1 < N and data[i + 1][j] == 'E':
                end = (i + 1, j, 1)
                data[i + 1][j] = data[i + 2][j] = data[i][j] = '0'
            elif j + 1 < N and data[i][j + 1] == 'E':
                end = (i, j + 1, 0)
                data[i][j + 1] = data[i][j + 2] = data[i][j] = '0'
while queue:
    ans += 1
    for i in range(len(queue)):
        x, y, stat = queue.pop(0)
        for d in range(5):
            check = True
            x_n, y_n = x + dx[d], y + dy[d]
            stat_n = (stat + ds[d]) % 2
            if stat != stat_n:
                if 0 <= x_n - 1 and x_n + 1 < N and 0 <= y_n - 1 and y_n + 1 < N:
                    if (x_n, y_n, stat_n) not in state:
                        for cx in range(x_n - 1, x_n + 2):
                            for cy in range(y_n - 1, y_n + 2):
                                if data[cx][cy] != '0':
                                    check = False
                                    break
                            if not check:
                                break
                        else:
                            state.add((x_n, y_n, stat_n))
                            queue.append((x_n, y_n, stat_n))
                            check = False
                            if (x_n, y_n, stat_n) == end:
                                check_end = True
                else:
                    check = False
            if check:
                if 0 <= x_n - stat_n and x_n + stat_n < N and 0 <= y_n - (1 - stat_n) and y_n + (1 - stat_n) < N:
                    if data[x_n - stat_n][y_n - (1 - stat_n)] == '0' and data[x_n + stat_n][y_n + (1 - stat_n)] == '0' and data[x_n][y_n] == '0':
                        if (x_n, y_n, stat_n) not in state:
                            state.add((x_n, y_n, stat_n))
                            queue.append((x_n, y_n, stat_n))
                            if (x_n, y_n, stat_n) == end:
                                check_end = True
    if check_end:
        break
if check_end:
    print(ans)
else:
    print(0)
