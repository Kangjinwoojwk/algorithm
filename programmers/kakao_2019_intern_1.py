def solution(board, moves):
    answer = 0
    bucket = list()
    n = len(board)
    for i in moves:
        j = 0
        while not board[j][i - 1]:
            j += 1
            if j == n:
                break
        if j == n:
            break
        if bucket and board[j][i - 1] == bucket[-1]:
            bucket.pop()
            answer += 2
        else:
            bucket.append(board[j][i - 1])
        board[j][i - 1] = 0
    return answer