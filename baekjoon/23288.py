from collections import deque
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]
dice = {'UU': 1, 'DD': 6, 'R': 3, 'L': 4, 'U': 2, 'D': 5}
N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
board_score = [[0] * M for _ in range(N)]
x, y = 0, 0
direction = 0
answer = 0

def score():
    for i in range(N):
        for j in range(M):
            if board_score != 0:
                visit = [[False] * M for _ in range(N)]
                queue = deque()
                cnt = 1
                visit[i][j] = True
                queue.append([i, j])
                board_score[i][j] = -1
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        if 0 <= x + dx[k] < N and 0 <= y + dy[k] < M and board[x + dx[k]][y + dy[k]] == board[i][j] and not visit[x + dx[k]][y + dy[k]]:
                            queue.append([x + dx[k],  y + dy[k]])
                            cnt += 1
                            visit[x + dx[k]][y + dy[k]] = True
                            board_score[x + dx[k]][y + dy[k]] = -1
                for x in range(N):
                    for y in range(M):
                        if board_score[x][y] == -1:
                            board_score[x][y] = cnt * board[x][y]


def roll_dice(direction):
    if direction == 0:
        dice['UU'], dice['R'], dice['DD'], dice['L'] = dice['L'], dice['UU'], dice['R'], dice['DD']
    elif direction == 1:
        dice['UU'], dice['D'], dice['DD'], dice['U'] = dice['U'], dice['UU'], dice['D'], dice['DD']
    elif direction == 2:
        dice['UU'], dice['R'], dice['DD'], dice['L'] = dice['R'], dice['DD'], dice['L'], dice['UU']
    elif direction == 3:
        dice['UU'], dice['D'], dice['DD'], dice['U'] = dice['D'], dice['DD'], dice['U'], dice['UU']

score()
for _ in range(K):
    if 0 <= x + dx[direction] < N and 0 <= y + dy[direction] < M:
        x, y = x + dx[direction], y + dy[direction]
        roll_dice(direction)
        if dice['DD'] > board[x][y]:
            direction = (direction - 1) % 4
        elif dice['DD'] < board[x][y]:
            direction = (direction + 1) % 4
        answer += board_score[x][y]
    else:
        direction = (direction + 2) % 4
        x, y = x + dx[direction], y + dy[direction]
        roll_dice(direction)
        if dice['DD'] > board[x][y]:
            direction = (direction - 1) % 4
        elif dice['DD'] < board[x][y]:
            direction = (direction + 1) % 4
        answer += board_score[x][y]
print(answer)