dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
N, M = map(int, input().split())
ans = 11


def sol(n, direction):
    global ans
    if n >= ans:
        return
    for i in range(4):



data = [list(input()) for _ in range(N)]
R = [0, 0]
B = [0, 0]
for i in range(N):
    for j in range(M):
        if data[i][j] == 'R':
            R = [i, j]
            data[i][j] = '.'
        elif data[i][j] == 'B':
            B = [i, j]
            data[i][j] = '.'
sol(0, 4)
if ans == 11:
    ans = -1
print(ans)