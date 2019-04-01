dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def sol(x, y, n, num):
    if n == 6:
        result.add(num)
        return
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < 4 and 0 <= ny < 4:
            sol(nx, ny, n + 1, num + data[nx][ny])

for tc in range(1, int(input()) + 1):
    data = [list(input().split()) for _ in range(4)]
    result = set()
    for i in range(4):
        for j in range(4):
            sol(i, j, 0, data[i][j])
    print('#{} {}'.format(tc, len(result)))