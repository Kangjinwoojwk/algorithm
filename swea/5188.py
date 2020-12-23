dx = [1, 0]
dy = [0, 1]
def sol(x, y, value):
    global N, ans
    value += data[x][y]
    if value >= ans:
        return
    if x == y == N - 1:
        if ans > value:
            ans = value
    for i in range(2):
        nx, ny = x + dx[i], y + dy[i]
        if nx < N and ny < N:
            sol(nx, ny, value)
T = int(input())
for tc in range(1, T + 1):
    ans = 2**30
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    sol(0, 0, 0)
    print('#{} {}'.format(tc, ans))