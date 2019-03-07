import sys
sys.stdin = open('4615.txt', 'r')
def get_dol(x, y, dol):
    global N
    board[y][x] = dol
    up = down = left = right = up_right = up_left = down_right = down_left = 0
    for i in range(1, N):
        if y - i < 0 or board[y - i][x] == None:
            break
        elif board[y - i][x] == dol:
            up = i
            break
    for i in range(1, N):
        if y + i == N or board[y + i][x] == None:
            break
        elif board[y + i][x] == dol:
            down = i
            break
    for i in range(1, N):
        if x - i < 0 or board[y][x - i] == None:
            break
        elif board[y][x - i] == dol:
            left = i
            break
    for i in range(1, N):
        if x + i == N or board[y][x + i] == None:
            break
        elif board[y][x + i] == dol:
            right = i
            break
    for i in range(1, N):
        if y - i < 0 or x - i < 0 or board[y - i][x - i] == None:
            break
        elif board[y - i][x - i] == dol:
            up_left = i
            break
    for i in range(1, N):
        if y - i < 0 or x + i == N or board[y - i][x + i] == None:
            break
        elif board[y - i][x + i] == dol:
            up_right = i
            break
    for i in range(1, N):
        if y + i == N or x - i < 0 or board[y + i][x - i] == None:
            break
        elif board[y + i][x - i] == dol:
            down_left = i
            break
    for i in range(1, N):
        if y + i == N or x + i == N or board[y + i][x + i] == None:
            break
        elif board[y + i][x + i] == dol:
            down_right = i
            break
    for i in range(1, up):
        board[y - i][x] = dol
    for i in range(1, down):
        board[y + i][x] = dol
    for i in range(1, left):
        board[y][x - i] = dol
    for i in range(1, right):
        board[y][x + i] = dol
    for i in range(1, up_left):
        board[y - i][x - i] = dol
    for i in range(1, up_right):
        board[y - i][x + i] = dol
    for i in range(1, down_left):
        board[y + i][x - i] = dol
    for i in range(1, down_right):
        board[y + i][x + i] = dol


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [[None] * N for _ in range(N)]
    board[N // 2 - 1][N // 2 - 1] = board[N // 2][N // 2] = 2
    board[N // 2 - 1][N // 2] = board[N // 2][N // 2 - 1] = 1
    for _ in range(M):
        x, y, dol = map(int, input().split())
        get_dol(x - 1, y - 1, dol)
    w = b = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                b += 1
            elif board[i][j] == 2:
                w += 1
    print('#{} {} {}'.format(tc, b, w))