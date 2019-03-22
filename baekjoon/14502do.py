dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def cal():
    global N, M
    for i in range(N):
        for j in range(M):
            pass
def sol(x, y, wall):
    global N, M
    if wall == 0:
        cal()
        return
    if x == N:
        return
    if data[x][y] == 0:
        data[x][y] = 1
        if y == M - 1:
            sol(x + 1, 0, wall - 1)
        else:
            sol(x, y + 1, wall - 1)
        data[x][y] = 0
    if y == M - 1:
        sol(x + 1, 0, wall)
    else:
        sol(x, y + 1, wall)
N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
ans = 0
sol(0, 0, 3)
print(ans)