T = int(input())
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]
for tc in range(1, T + 1):
    N = int(input())
    data_map = [[0, 0] * 4001 for _ in range(4001)]
    ans = 0
    qu = []
    for _ in range(N):
        x, y, move, K = map(int, input().split())
        data_map[2 * (x + 1000)][2 * (y + 1000)][0] = K
        data_map[2 * (x + 1000)][2 * (y + 1000)][1] = _
        qu.append([2 * (x + 1000), 2 * (y + 1000), move])
    while N > 0:
        cnt = 0
        delete_idx = []
        del_cnt = 0
        for i in range(N):
            for j in range(4):
                if j == qu[i][2]:
                    p_x, p_y = qu[i][0], qu[i][1]
                    x, y = p_x + dx[j], p_y + dy[j]
                    if qu[i][2] == 0:
                        if p_y == 4000:
                            data_map[p_x][p_y][0] =data_map[p_x][p_y][1] = 0
                            N -= 1
                            continue
                    elif qu[i][2] == 1:
                        if p_y == 0:
                            data_map[p_x][p_y][0] = data_map[p_x][p_y][1] = 0
                            N -= 1
                            continue
                    elif qu[i][2] == 2:
                        if p_x == 0:
                            data_map[p_x][p_y][0] = data_map[p_x][p_y][1] = 0
                            N -= 1
                            continue
                    elif qu[i][2] == 3:
                        if p_x == 4000:
                            data_map[p_x][p_y][0] = data_map[p_x][p_y][1] = 0
                            N -= 1
                            continue
                    if data_map[x][y][0] == 0:
                        data_map[x][y][0], data_map[p_x][p_y][0] = data_map[p_x][p_y][0], data_map[x][y][0]
                        data_map[x][y][1], data_map[p_x][p_y][1] = data_map[p_x][p_y][1], data_map[x][y][1]
                        qu[i][0], qu[i][1] = x, y
                    else:
                        data_map[x][y][0] += data_map[p_x][p_y][0]
                        data_map[p_x][p_y][1] = 0
                        qu[i][0], qu[i][1] = x, y
                        delete_idx.append(i)
                        del_cnt += 1
                        if data_map[x][y][1] not in delete_idx:
                            delete_idx.append(data_map[x][y][1])
                            del_cnt += 1
        delete_idx.sort(reverse=True)
        for i in range(del_cnt):
            N -= 1
            x, y = qu[delete_idx[i]][0], qu[delete_idx[i]][1]
            ans += data_map[x][y][0]
            data_map[x][y][0] = 0
            data_map[x][y][1] = 0
            qu.remove(delete_idx[i])

