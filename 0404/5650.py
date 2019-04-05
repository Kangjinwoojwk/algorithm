dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for tc in range(1, int(input()) + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    hall = {
        6: list(),
        7: list(),
        8: list(),
        9: list(),
        10: list()
    }
    ans = 0
    for i in range(N):
        for j in range(N):
            if data[i][j] >= 6:
                hall[data[i][j]].append((i, j))
    for i in range(6, 11):
        if hall[i]:
            hall[hall[i][0]] = hall[i][1]
            hall[hall[i][1]] = hall[i][0]
    for i in range(N):
        for j in range(N):
            if data[i][j] == 0:
                for k in range(4):
                    Q = [(i + dx[k], j + dy[k], k)]
                    cnt = 0
                    while Q:
                        x, y, direction = Q.pop()
                        if x == i and y == j:
                            break
                        if x < 0 or x >= N or y < 0 or y >= N:
                            cnt = (cnt << 1) + 1
                            break
                        elif data[x][y] == 5:
                            cnt = (cnt << 1) + 1
                            break
                        elif data[x][y] == -1:
                            break
                        elif data[x][y] == 1:
                            if direction == 0 or direction == 1:
                                cnt = (cnt << 1) + 1
                                break
                            else:
                                cnt += 1
                                if direction == 3:
                                    direction = 0
                                elif direction == 2:
                                    direction = 1
                        elif data[x][y] == 2:
                            if direction == 2 or direction == 1:
                                cnt = (cnt << 1) + 1
                                break
                            else:
                                cnt += 1
                                if direction == 0:
                                    direction = 1
                                elif direction == 3:
                                    direction = 2
                        elif data[x][y] == 3:
                            if direction == 2 or direction == 3:
                                cnt = (cnt << 1) + 1
                                break
                            else:
                                cnt += 1
                                if direction == 0:
                                    direction = 3
                                elif direction == 1:
                                    direction = 2
                        elif data[x][y] == 4:
                            if direction == 0 or direction == 3:
                                cnt = (cnt << 1) + 1
                                break
                            else:
                                cnt += 1
                                if direction == 2:
                                    direction = 3
                                elif direction == 1:
                                    direction = 0
                        elif data[x][y] > 5:
                            x, y = hall[(x, y)]
                        x, y = x + dx[direction], y + dy[direction]
                        Q.append((x, y, direction))
                    if cnt > ans:
                        ans = cnt
    print('#{} {}'.format(tc, ans))