def solution(board):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    answer = 0
    N = len(board)
    visit = {(0, 1, 0)}
    queue = [(0, 1, 0)]
    while (N - 1, N - 1, 0) not in visit and (N - 1, N - 1, 1) not in visit:
        answer += 1
        for _ in range(len(queue)):
            x, y, d = queue.pop(0)
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx - d and nx < N and 0 <= ny - 1 + d and ny < N:
                    if board[nx][ny] == 0 and board[nx - d][ny - 1 + d] == 0 and (nx, ny, d) not in visit:
                        visit.add((nx, ny, d))
                        queue.append((nx, ny, d))
            if d == 0:
                if x + 1 < N and board[x + 1][y] == 0 and board[x + 1][y - 1] == 0:
                    if (x + 1, y - 1, 1) not in visit:
                        visit.add((x + 1, y - 1, 1))
                        queue.append((x + 1, y - 1, 1))
                    if (x + 1, y, 1) not in visit:
                        visit.add((x + 1, y, 1))
                        queue.append((x + 1, y, 1))
                if x - 1 >= 0 and board[x - 1][y] == 0 and board[x - 1][y - 1] == 0:
                    if (x, y - 1, 1) not in visit:
                        visit.add((x, y - 1, 1))
                        queue.append((x, y - 1, 1))
                    if (x, y, 1) not in visit:
                        visit.add((x, y, 1))
                        queue.append((x, y, 1))
            else:
                if y + 1 < N and board[x - 1][y + 1] == 0 and board[x][y + 1] == 0:
                    if (x - 1, y + 1, 0) not in visit:
                        visit.add((x - 1, y + 1, 0))
                        queue.append((x - 1, y + 1, 0))
                    if (x, y + 1, 0) not in visit:
                        visit.add((x, y + 1, 0))
                        queue.append((x, y + 1, 0))
                if y - 1 >= 0 and board[x - 1][y - 1] == 0 and board[x][y - 1] == 0:
                    if (x - 1, y, 0) not in visit:
                        visit.add((x - 1, y, 0))
                        queue.append((x - 1, y, 0))
                    if (x, y, 0) not in visit:
                        visit.add((x, y, 0))
                        queue.append((x, y, 0))
    return answer