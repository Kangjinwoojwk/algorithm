import sys
sys.stdin = open('4875.txt', 'r')
sys.stdout = open('4875_out.txt', 'w')
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def sol(x, y, maze, maze_map, N):
    for i in range(4):
        if 0 <= x + dx[i] < N and 0 <= y + dy[i] < N:
            if maze_map[x + dx[i]][y + dy[i]] == False and maze[x + dx[i]][y + dy[i]] != 1:
                maze_map[x + dx[i]][y + dy[i]] = True
                sol(x + dx[i], y + dy[i], maze, maze_map, N)
    return


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)]
    x = y = end_x = end_y = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                x, y = i, j
            if maze[i][j] == 3:
                end_x, end_y = i, j
    maze_map = [[False] * N for _ in range(N)]
    maze_map[x][y] = True
    sol(x, y, maze, maze_map, N)
    if maze_map[end_x][end_y]:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')
