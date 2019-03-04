dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
R, C = map(int, input().split())
board = [input() for _ in range(R)]
visited = [True] * 26
