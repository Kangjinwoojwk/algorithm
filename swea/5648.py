import sys
sys.stdin = open('5648.txt', 'r')
T = int(input())
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for _ in range(N):
        data[_][0] *= 2
        data[_][1] *= 2
    while N > 0:
        chk = dict()
        delete_li = []
        delete_cnt = 0
        for i in range(N):
            data[i][0] += dx[data[i][2]]
            data[i][1] += dy[data[i][2]]
            if (data[i][0], data[i][1]) not in chk:
                chk[(data[i][0], data[i][1])] = 1
            else:
                chk[(data[i][0], data[i][1])] += 1
        for i in range(N):
            if data[i][0] < -2000 or data[i][1] < -2000 or data[i][0] > 2000 or data[i][1] > 2000:
                delete_cnt += 1
                delete_li.append(i)
            elif chk[(data[i][0], data[i][1])] > 1:
                ans += data[i][3]
                delete_cnt += 1
                delete_li.append(i)
        for i in range(delete_cnt - 1, -1, -1):
            data.pop(delete_li[i])
            N -= 1
    print('#{} {}'.format(tc, ans))





# 이 방식은 시간이 터진다. 근데 시간 터지기 전에 메모리도 터진다....어디서 터지는거지?
# T = int(input())
# dy = [1, -1, 0, 0]
# dx = [0, 0, -1, 1]
# for tc in range(1, T + 1):
#     N = int(input())
#     data_map = [[[0] * 2 for _ in range(4001)] for _ in range(4001)]
#     ans = 0
#     qu = []
#     for _ in range(N):
#         x, y, move, K = map(int, input().split())
#         data_map[2 * (x + 1000)][2 * (y + 1000)][0] = K
#         data_map[2 * (x + 1000)][2 * (y + 1000)][1] = _
#         qu.append([2 * (x + 1000), 2 * (y + 1000), move])
#     while N > 0:
#         cnt = 0
#         delete_idx = []
#         del_cnt = 0
#         for i in range(N):
#             for j in range(4):
#                 if j == qu[i][2]:
#                     p_x, p_y = qu[i][0], qu[i][1]
#                     x, y = p_x + dx[j], p_y + dy[j]
#                     if qu[i][2] == 0:
#                         if p_y == 4000:
#                             data_map[p_x][p_y][0] = data_map[p_x][p_y][1] = 0
#                             N -= 1
#                             delete_idx.append(i)
#                             continue
#                     elif qu[i][2] == 1:
#                         if p_y == 0:
#                             data_map[p_x][p_y][0] = data_map[p_x][p_y][1] = 0
#                             N -= 1
#                             delete_idx.append(i)
#                             continue
#                     elif qu[i][2] == 2:
#                         if p_x == 0:
#                             data_map[p_x][p_y][0] = data_map[p_x][p_y][1] = 0
#                             N -= 1
#                             delete_idx.append(i)
#                             continue
#                     elif qu[i][2] == 3:
#                         if p_x == 4000:
#                             data_map[p_x][p_y][0] = data_map[p_x][p_y][1] = 0
#                             N -= 1
#                             delete_idx.append(i)
#                             continue
#                     if data_map[x][y][0] == 0:
#                         data_map[x][y][0], data_map[p_x][p_y][0] = data_map[p_x][p_y][0], data_map[x][y][0]
#                         data_map[x][y][1], data_map[p_x][p_y][1] = data_map[p_x][p_y][1], data_map[x][y][1]
#                         qu[i][0], qu[i][1] = x, y
#                     else:
#                         data_map[x][y][0] += data_map[p_x][p_y][0]
#                         data_map[p_x][p_y][1] = 0
#                         qu[i][0], qu[i][1] = x, y
#                         delete_idx.append(i)
#                         del_cnt += 1
#                         if data_map[x][y][1] not in delete_idx:
#                             delete_idx.append(data_map[x][y][1])
#                             del_cnt += 1
#         delete_idx.sort(reverse=True)
#         for i in range(del_cnt):
#             N -= 1
#             x, y = qu[delete_idx[i]][0], qu[delete_idx[i]][1]
#             ans += data_map[x][y][0]
#             data_map[x][y][0] = 0
#             data_map[x][y][1] = 0
#             qu.pop(delete_idx[i])
#     print('#{} {}'.format(tc, ans))
