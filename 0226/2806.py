def get_queen(cnt, x, y):
    global N
    for i in range(N):
        chess_map[cnt][x][i] = False
        chess_map[cnt][i][y] = False
        if x + i < N and y + i < N:
            chess_map[cnt][x + i][y + i] = False
        if x - i >= 0 and y + i < N:
            chess_map[cnt][x - i][y + i] = False
        if x + i < N and y - i >= 0:
            chess_map[cnt][x + i][y - i] = False
        if x - i >= 0 and y - i >= 0:
            chess_map[cnt][x - i][y - i] = False


def sol(cnt):
    global ans
    global N
    if cnt == N:
        ans += 1
        return
    for i in range(N):
        chess_map[cnt + 1] = [chess_map[cnt][i][:] for i in range(N)]
        if chess_map[cnt + 1][cnt][i]:
            get_queen(cnt + 1, cnt, i)
            sol(cnt + 1)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    ans = 0
    chess_map = [[[True] * N for _ in range(N)]for _ in range(N + 1)]
    sol(0)
    print('#{} {}'.format(test_case, ans))
