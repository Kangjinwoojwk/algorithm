dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
for tc in range(1, int(input()) + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    max_move = 0
    ans = 0
    for i in range(N):
        for j in range(N):
            st = list()
            st.append((i, j))
            move = 1
            while st:
                x, y = st.pop()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if data[nx][ny] == data[x][y] + 1:
                            st.append((nx, ny))
                            move += 1
            if move > max_move:
                max_move = move
                ans = data[i][j]
            elif move == max_move and ans > data[i][j]:
                ans = data[i][j]
    print('#{} {} {}'.format(tc, ans, max_move))
