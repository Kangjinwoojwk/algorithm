dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
R, C, N = map(int, input().split())
data = [list(input()) for _ in range(R)]
full = [['O'] * C for _ in range(R)]
ans = [['O'] * C for _ in range(R)]
if N == 0 or N == 1:
    for i in range(R):
        print(''.join(data[i]))
elif N % 2 == 0:
    for i in range(R):
        print(''.join(full[i]))
else:
    while N - 1:
        ans = [['O'] * C for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if data[i][j] == 'O':
                    ans[i][j] = '.'
                    for k in range(4):
                        x, y = i + dx[k], j + dy[k]
                        if 0 <= x < R and 0 <= y < C:
                            ans[x][y] = '.'
        N -= 2
        data = ans
    for i in range(R):
        print(''.join(data[i]))
