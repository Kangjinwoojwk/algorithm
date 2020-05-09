# 도로만들기 코너와 직선 가격 다름 가장 작은 가격에 끝에서 끝은? 시간 초과 실패가 다수 있는 코드

from queue import PriorityQueue

def solution(board):
    size = len(board)
    answer = size * size * 500
    move = [(0, 0), (0, 1), (1, 0), (0, -1), (-1, 0)]
    bfs = PriorityQueue()
    bfs.put((0, 0, 0, 1))
    bfs.put((0, 0, 0, 2))
    while bfs:
        cost, x, y, direction = bfs.get()
        if x == size - 1 and y == size - 1:
            answer = cost
            break
        if cost > answer:
            pass
        for i in range(1, 5):
            if direction + 2 == i or direction - 2 == i:
                pass
            dx, dy = move[i]
            if 0 <= x + dx < size and 0 <= y + dy < size and board[x + dx][y + dy] == 0:
                if direction == i:
                    bfs.put((cost + 100, x + dx, y + dy, i))
                else:
                    bfs.put((cost + 600, x + dx, y + dy, i))

    return answer