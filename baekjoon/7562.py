T = int(input())
dx = [-1, -1, 1, 1, -2, -2, 2, 2]
dy = [-2, 2, -2, 2, 1, -1, 1, -1]
for test_case in range(T):
    I = int(input())
    start_x, start_y = map(int, input().split())
    goal_x, goal_y = map(int, input().split())
    ans = 0
    chess_map = [[0] * I for _ in range(I)]
    chess_map[start_x][start_y] = 1
    dummy_map = [[0] * I for _ in range(I)]
    while chess_map[goal_x][goal_y] == 0:
        for i in range(I):
            for j in range(I):
                if chess_map[i][j] == 1:
                    for k in range(8):
                        if 0 <= i + dx[k] < I and 0 <= j + dy[k] < I:
                            dummy_map[i + dx[k]][j + dy[k]] = 1
        for i in range(I):
            for j in range(I):
                if dummy_map[i][j] == 1:
                    chess_map[i][j] = 1
        ans += 1
    print(ans)
