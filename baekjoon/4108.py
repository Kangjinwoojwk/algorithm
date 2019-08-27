dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
while True:
    R, C = map(int, input().split())
    if R == C == 0:
        break
    data = [list(input()) for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if data[i][j] == '.':
                data[i][j] = 0
    for i in range(R):
        for j in range(C):
            if data[i][j] == '*':
                for k in range(8):
                    x, y = i + dx[k], j + dy[k]
                    if 0 <= x < R and 0 <= y < C and data[x][y] != '*':
                        data[x][y] += 1
    for i in data:
        print(''.join(map(str, i)))

