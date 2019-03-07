dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def get_danji(x, y, danji):
    global N
    apt[x][y] = danji
    cnt[danji] += 1
    for i in range(4):
        n_x, n_y = x + dx[i], y + dy[i]
        if 0 <= n_x < N and 0 <= n_y < N:
            if apt[n_x][n_y] == '1':
                get_danji(n_x, n_y, danji)
N = int(input())
apt = [list(input()) for _ in range(N)]
cnt = [0]
danji = 1
for i in range(N):
    for j in range(N):
        if apt[i][j] == '1':
            cnt.append(0)
            get_danji(i, j, danji)
            danji += 1
print(danji - 1)
cnt.sort()
for i in range(1, danji):
    print(cnt[i])