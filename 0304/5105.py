import sys
sys.stdin = open('5105.txt', 'r')
sys.stdout = open('5105_out.txt', 'w')
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def sol(x, y, step, maze, maze_map, N, ans):
    if maze[x][y] == 3:
        ans[0] = step - 1
    for i in range(4):
        if 0 <= x + dx[i] < N and 0 <= y + dy[i] < N:
            if maze_map[x + dx[i]][y + dy[i]] is False and maze[x + dx[i]][y + dy[i]] != 1:
                maze_map[x + dx[i]][y + dy[i]] = True
                sol(x + dx[i], y + dy[i], step + 1, maze, maze_map, N, ans)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)]
    x = y = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                x = i
                y = j
    maze_map = [[False] * N for _ in range(N)]
    maze_map[x][y] = True
    ans = [0]
    sol(x, y, 0, maze, maze_map, N, ans)
    print('#{} {}'.format(test_case, ans[0]))


