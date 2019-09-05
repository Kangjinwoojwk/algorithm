dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
def cal(start, end):
    global ans
    visit = [[[True] * 5 for _ in range(5)] for _ in range(5)]
    queue = [start]
    visit[start[0]][start[1]][start[2]] = False
    step = 0
    while queue:
        step += 1
        if step >= ans:
            return
        for _ in range(len(queue)):
            x, y, z = queue.pop(0)
            if (x, y, z) == end:
                if ans > step - 1:
                    ans = step - 1
                return
            for i in range(6):
                nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
                if 0 <= nx < 5 and 0 <= ny < 5 and 0 <= nz < 5 and cube[nx][ny][nz] and visit[nx][ny][nz]:
                    visit[nx][ny][nz] = False
                    queue.append((nx, ny, nz))


def copy(cube_pan, pan, direction):
    if ans == 12:
        return
    if direction == 0:
        for i in range(5):
            for j in range(5):
                cube[cube_pan][i][j] = data[pan][i][j]
    elif direction == 1:
        for i in range(5):
            for j in range(5):
                cube[cube_pan][i][j] = data[pan][4 - j][i]
    elif direction == 2:
        for i in range(5):
            for j in range(5):
                cube[cube_pan][i][j] = data[pan][4 - i][4 - j]
    elif direction == 3:
        for i in range(5):
            for j in range(5):
                cube[cube_pan][i][j] = data[pan][j][4 - i]


def create():
    if ans == 12:
        return
    for i in range(5):
        copy(i, per[i], d[per[i]])
    if cube[0][0][0] and cube[4][4][4]:
        cal((0, 0, 0), (4, 4, 4))
    if cube[0][0][4] and cube[4][4][0]:
        cal((0, 0, 4), (4, 4, 0))
    if cube[0][4][4] and cube[4][0][0]:
        cal((0, 4, 4), (4, 0, 0))
    if cube[4][0][4] and cube[0][4][0]:
        cal((4, 0, 4), (0, 4, 0))


def permutation(n):
    if ans == 12:
        return
    if n == 0:
        create()
        return
    for i in range(n):
        per[i], per[n - 1] = per[n - 1], per[i]
        permutation(n - 1)
        per[n - 1], per[i] = per[i], per[n - 1]


def sol(n):
    if ans == 12:
        return
    if n == -1:
        permutation(5)
        return
    for i in range(4):
        d[n] = i
        sol(n - 1)

ans = 100000
data = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
cube = [[[0] * 5 for _ in range(5)] for _ in range(5)]
per = [_ for _ in range(5)]
d = [0] * 5
sol(4)
if ans == 100000:
    ans = -1
print(ans)