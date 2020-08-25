def solution(board, moves):
    answer = 0
    n = len(board)
    bucket = list()
    for i in moves:
        i -= 1
        for j in range(n):
            if board[j][i]:
                if bucket and bucket[-1] == board[j][i]:
                    bucket.pop()
                    answer += 2
                else:
                    bucket.append(board[j][i])
                board[j][i] = 0
                break
    return answer