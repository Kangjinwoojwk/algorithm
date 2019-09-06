def solution(board):
    answer = [0]
    block = set()
    N = len(board)
    def check(x, y, block, answer):
        if y + 2 < N and x + 1 < N and board[x][y] == board[x][y + 1] == board[x][y + 2] == board[x + 1][y + 2]:
            board[x][y] = board[x][y + 1] = board[x][y + 2] = board[x + 1][y + 2] = 0
            block.add(y)
            block.add(y + 1)
            block.add(y + 2)
        elif y + 1 < N and x + 2 < N and board[x][y] == board[x][y + 1] == board[x + 2][y] == board[x + 1][y]:
            board[x][y] = board[x][y + 1] = board[x + 2][y] = board[x + 1][y] = 0
            block.add(y)
            block.add(y + 1)
        elif y + 2 < N and x + 1 < N and board[x][y] == board[x][y + 1] == board[x][y + 2] == board[x + 1][y]:
            board[x][y] = board[x][y + 1] = board[x][y + 2] = board[x + 1][y] = 0
            block.add(y)
            block.add(y + 1)
            block.add(y + 2)
        elif y + 1 < N and x + 2 < N and board[x][y] == board[x][y + 1] == board[x + 2][y + 1] == board[x + 1][y + 1]:
            board[x][y] = board[x][y + 1] = board[x + 2][y + 1] = board[x + 1][y + 1] = 0
            block.add(y)
            block.add(y + 1)
        elif y + 2 < N and x + 1 < N and board[x][y] == board[x][y + 1] == board[x][y + 2] == board[x + 1][y + 1]:
            board[x][y] = board[x][y + 1] = board[x][y + 2] = board[x + 1][y + 1] = 0
            block.add(y)
            block.add(y + 1)
            block.add(y + 2)
        elif y + 1 < N and x + 2 < N and board[x][y] == board[x + 1][y + 1] == board[x + 1][y] == board[x + 2][y]:
            board[x][y] = board[x + 1][y + 1] = board[x + 1][y] = board[x + 2][y] = 0
            block.add(y)
            block.add(y + 1)
        elif y - 1 >= 0 and x + 2 < N and board[x][y] == board[x + 1][y - 1] == board[x + 1][y] == board[x + 2][y]:
            board[x][y] = board[x + 1][y - 1] = board[x + 1][y] = board[x + 2][y] = 0
            block.add(y)
            block.add(y - 1)
        else:
            if x + 1 < N and y + 2 < N and board[x][y] == board[x + 1][y] == board[x + 1][y + 1] == board[x + 1][y + 2]:
                if board[x][y + 1]:
                    check(x, y + 1, block, answer)
                if board[x][y + 2]:
                    check(x, y + 2, block, answer)
                if y + 1 not in block and y + 2 not in block:
                    answer[0] += 1
                else:
                    block.add(y)
                    block.add(y + 1)
                    block.add(y + 2)
                board[x][y] = board[x + 1][y] = board[x + 1][y + 1] = board[x + 1][y + 2] = 0
            elif x + 2 < N and y - 1 >= 0 and board[x][y] == board[x + 1][y] == board[x + 2][y] == board[x + 2][y - 1]:
                if board[x + 1][y - 1]:
                    if y - 3 >= 0 and board[x + 1][y - 1] == board[x + 1][y - 3]:
                        check(x + 1, y - 3, block, answer)
                    if y - 2 >= 0 and board[x + 1][y - 1] == board[x + 1][y - 2]:
                        check(x + 1, y - 2, block, answer)
                if y - 1 not in block:
                    answer[0] += 1
                else:
                    block.add(y)
                    block.add(y - 1)
                board[x][y] = board[x + 1][y] = board[x + 2][y] = board[x + 2][y - 1] = 0
            elif x + 2 < N and y + 1 < N and board[x][y] == board[x + 1][y] == board[x + 2][y] == board[x + 2][y + 1]:
                if board[x][y + 1]:
                    check(x, y + 1, block, answer)
                if board[x + 1][y + 1]:
                    if y + 2 < N and board[x + 1][y + 1] == board[x][y + 2]:
                        check(x, y + 2, block, answer)
                    elif y + 3 < N and board[x + 1][y + 1] == board[x][y + 3]:
                        check(x, y + 3, block, answer)
                    else:
                        check(x + 1, y + 1, block, answer)
                if y + 1 not in block:
                    answer[0] += 1
                else:
                    block.add(y)
                    block.add(y + 1)
                board[x][y] = board[x + 1][y] = board[x + 2][y] = board[x + 2][y + 1] = 0
            elif x + 1 < N and y - 2 >= 0 and board[x][y] == board[x + 1][y] == board[x + 1][y - 1] == board[x + 1][
                y - 2]:
                if y - 1 not in block and y - 2 not in block:
                    answer[0] += 1
                else:
                    block.add(y)
                    block.add(y - 1)
                    block.add(y - 2)
                board[x][y] = board[x + 1][y] = board[x + 1][y - 1] = board[x + 1][y - 2] = 0
            elif x + 1 < N and y - 1 >= 0 and y + 1 < N and board[x][y] == board[x + 1][y - 1] == board[x + 1][y] == \
                    board[x + 1][y + 1]:
                if board[x][y + 1]:
                    check(x, y + 1, block, answer)
                if y - 1 not in block and y + 1 not in block:
                    answer[0] += 1
                else:
                    block.add(y)
                    block.add(y - 1)
                    block.add(y + 1)
                board[x][y] = board[x + 1][y - 1] = board[x + 1][y] = board[x + 1][y + 1] = 0

    for i in range(N):
        for j in range(N):
            if board[i][j]:
                check(i, j, block, answer)

    return answer[0]


bo = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 0, 0, 0], [0, 0, 0, 0, 0, 4, 4, 0, 0, 0], [0, 0, 0, 0, 3, 0, 4, 0, 0, 0], [0, 0, 0, 2, 3, 0, 0, 0, 5, 5], [1, 2, 2, 2, 3, 3, 0, 0, 0, 5], [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]]
print(solution(bo))