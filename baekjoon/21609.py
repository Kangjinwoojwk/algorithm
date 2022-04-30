from collections import deque
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visit = [[True] * N for _ in range(N)]
answer = 0
def gravity():
    for i in range(N):
        root = N - 1
        for j in range(N - 1, -1, -1):
            if board[j][i] == '':
                continue
            elif board[j][i] >= 0:
                board[root][i], board[j][i] = board[j][i], board[root][i]
                root -= 1
            elif board[j][i] == -1:
                root = j - 1


def spin():
    for i in range(N//2):
        for j in range(i, N - 1 - i):
            board[i][j], board[j][N - 1 - i], board[N - 1 - i][N - 1 - j], board[N - 1 - j][i] = board[j][N - 1 - i], board[N - 1 - i][N - 1 - j], board[N - 1 - j][i], board[i][j]


def select(x, y):
    chk = board[x][y]
    queue = deque()
    visit[x][y] = False
    board[x][y] = ''
    queue.append((x, y))
    while queue:
        temp_x, temp_y = queue.popleft()
        for i in range(4):
            if 0 <= temp_x + dr[i] < N and 0 <= temp_y + dc[i] < N and visit[temp_x + dr[i]][temp_y + dc[i]] and board[temp_x + dr[i]][temp_y + dc[i]] in (chk, 0):
                board[temp_x + dr[i]][temp_y + dc[i]] = ''
                queue.append((temp_x + dr[i], temp_y + dc[i]))


def chk_size(x, y):
    size = 1
    queue = deque()
    visit[x][y] = False
    queue.append((x, y))
    chk_rainbow = list()
    while queue:
        temp_x, temp_y = queue.popleft()
        for i in range(4):
            if 0 <= temp_x + dr[i] < N and 0 <= temp_y + dc[i] < N and visit[temp_x + dr[i]][temp_y + dc[i]] and board[temp_x + dr[i]][temp_y + dc[i]] in (board[x][y], 0):
                size += 1
                visit[temp_x + dr[i]][temp_y + dc[i]] = False
                queue.append((temp_x + dr[i], temp_y + dc[i]))
                if board[temp_x + dr[i]][temp_y + dc[i]] == 0:
                    chk_rainbow.append((temp_x + dr[i], temp_y + dc[i]))
    rainbow = len(chk_rainbow)
    for i in chk_rainbow:
        visit[i[0]][i[1]] = True
    return size, rainbow, x, y


while True:
    curr = [-1, -1, -1, -1]
    for i in range(N):
        for j in range(N):
            if visit[i][j] and board[i][j] not in ('', -1, 0):
                size, rainbow, x, y = chk_size(i, j)
                if size > curr[0]:
                    curr = [size, rainbow, x, y]
                elif size == curr[0]:
                    if rainbow >= curr[1]:
                        curr = [size, rainbow, x, y]
    if curr[0] < 2:
        break
    visit = [[True] * N for _ in range(N)]
    select(curr[2], curr[3])
    answer += curr[0] * curr[0]
    visit = [[True] * N for _ in range(N)]
    gravity()
    spin()
    gravity()
print(answer)

