dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
N, M = map(int, input().split())
data = [list(input()) for _ in range(N)]
ans = 11
axis = list()


def sol(n, direction):
    global ans
    if n >= ans:
        return
    


for i in range(N):
    for j in range(M):
        if data[i][j] == 'R' or data[i][j] == 'B':
            axis.append([i, j])
for i in range(4):
    sol(1, i)
if ans == 11:
    ans = -1
print(ans)