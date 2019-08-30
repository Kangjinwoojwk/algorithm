dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
N, M, x, y, K = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
dice = {
    'U': 0,
    'D': 0,
    'L': 0,
    'R': 0,
    'F': 0,
    'B': 0,
}
move = list(map(int, input().split()))
for i in move:
    nx, ny = x + dx[i], y + dy[i]
    if not (0 <= nx < N and 0 <= ny < M):
        continue
    if i == 1:
        dice['U'], dice['R'], dice['D'], dice['L'] = \
            dice['R'], dice['D'], dice['L'], dice['U']
    elif i == 2:
        dice['R'], dice['D'], dice['L'], dice['U'] = \
            dice['U'], dice['R'], dice['D'], dice['L']
    elif i == 3:
        dice['U'], dice['F'], dice['D'], dice['B'] = \
            dice['F'], dice['D'], dice['B'], dice['U']
    elif i == 4:
        dice['F'], dice['D'], dice['B'], dice['U'] = \
            dice['U'], dice['F'], dice['D'], dice['B']
    if data[nx][ny]:
        dice['D'] = data[nx][ny]
        data[nx][ny] = 0
    else:
        data[nx][ny] = dice['D']
    print(dice['U'])
    x, y = nx, ny