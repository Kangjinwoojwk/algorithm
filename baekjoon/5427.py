# 하...뭔가 했더니 불을 먼저 해줘야 한다. 이제 불 붙을 곳으로는 못움직인다는 걸 안 읽었다...ㅠㅠ
T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for test_case in range(T):
    garo, sero = map(int, input().split())
    building = [list(input()) for _ in range(sero)]
    sang_queue = []
    fire_queue = []
    sang_cnt = 0
    fire_cnt = 0
    for i in range(sero):
        for j in range(garo):
            if building[i][j] == '@':
                sang_queue.append([i, j])
                sang_cnt += 1
            elif building[i][j] == '*':
                fire_queue.append([i, j])
                fire_cnt += 1
    sang_start, sang_end = 0, sang_cnt
    fire_start, fire_end = 0, fire_cnt
    chk = True
    step = 1
    if sang_queue[0][0] == 0 or sang_queue[0][1] == 0 or sang_queue[0][0] == sero - 1 or sang_queue == garo - 1:
        chk = False
    while chk:
        sang_cnt = fire_cnt = 0
        for i in range(fire_start, fire_end):
            for j in range(4):
                x, y = fire_queue[i][0] + dx[j], fire_queue[i][1] + dy[j]
                if x < 0 or y < 0 or x >= sero or y >= garo:
                    continue
                if building[x][y] == '#' or building[x][y] == '*':
                    continue
                building[x][y] = '*'
                fire_queue.append([x, y])
                fire_cnt += 1
        for i in range(sang_start, sang_end):
            for j in range(4):
                x, y = sang_queue[i][0] + dx[j], sang_queue[i][1] + dy[j]
                if x < 0 or y < 0 or x >= sero or y >= garo:
                    continue
                if building[x][y] == '#' or building[x][y] == '*' or building[x][y] == '@':
                    continue
                if x == 0 or y == 0 or x == sero - 1 or y == garo - 1:
                    chk = False
                    continue
                building[x][y] = '@'
                sang_queue.append([x, y])
                sang_cnt += 1
        step += 1
        if sang_cnt == 0:
            break
        sang_start, sang_end = sang_end, sang_end + sang_cnt
        fire_start, fire_end = fire_end, fire_end + fire_cnt
    if chk:
        print('IMPOSSIBLE')
    else:
        print(step)


# T = int(input())
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# for test_case in range(T):
#     garo, sero = map(int, input().split())
#     building = [list(input()) for _ in range(sero)]
#     sang_queue = []
#     fire_queue = []
#     for i in range(sero):
#         for j in range(garo):
#             if building[i][j] == '@':
#                 sang_queue.append([i, j])
#             elif building[i][j] == '*':
#                 fire_queue.append([i, j])
#     sang_start, sang_end = 0, len(sang_queue)
#     fire_start, fire_end = 0, len(fire_queue)
#     chk = True
#     step = 1
#     if sang_queue[0][0] == 0 or sang_queue[0][1] == 0 or sang_queue[0][0] == sero - 1 or sang_queue == garo - 1:
#         chk = False
#     while chk:
#         if sang_start == sang_end:
#             break
#         for i in range(sang_start, sang_end):
#             for j in range(4):
#                 x, y = sang_queue[i][0] + dx[j], sang_queue[i][1] + dy[j]
#                 if 0 <= x < sero and 0 <= y < garo and building[x][y] == '.':
#                     building[x][y] = '@'
#                     if x == 0 or y == 0 or x == sero - 1 or y == garo - 1:
#                         chk = False
#                     sang_queue.append([x, y])
#         for i in range(fire_start, fire_end):
#             for j in range(4):
#                 x, y = fire_queue[i][0] + dx[j], fire_queue[i][1] + dy[j]
#                 if 0 <= x < sero and 0 <= y < garo:
#                     if building[x][y] == '.' or building[x][y] == '@':
#                         building[x][y] = '*'
#                         fire_queue.append([x, y])
#         step += 1
#         sang_start, sang_end = sang_end, len(sang_queue)
#         fire_start, fire_end = fire_end, len(fire_queue)
#     if chk:
#         print('IMPOSSIBLE')
#     else:
#         print(step)



# T = int(input())
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# for test_case in range(T):
#     garo, sero = map(int, input().split())
#     building = [list(input()) for _ in range(sero)]
#     sang_queue = []
#     fire_queue = []
#     chk = False
#     step = 1
#     while chk == False:
#         for i in range(sero):
#             for j in range(garo):
#                 if building[i][j] == '@':
#                     for k in range(4):
#                         if 0 <= i + dx[k] < sero and 0 <= j + dy[k] < garo and building[i + dx[k]][j + dy[k]] == '.':
#                             sang_queue.append([i + dx[k], j + dy[k]])
#                 elif building[i][j] == '*':
#                     for k in range(4):
#                         if 0 <= i + dx[k] < sero and 0 <= j + dy[k] < garo and building[i + dx[k]][j + dy[k]] == '.':
#                             fire_queue.append([i + dx[k], j + dy[k]])
#         for i in sang_queue:
#             if i[0] == 0 or i[0] == sero - 1 or i[1] == 0 or i[1] == garo - 1:
#                 chk = True
#             building[i[0]][i[1]] = '@'
#         for i in fire_queue:
#             building[i[0]][i[1]] = '*'
#         step += 1
#         if sang_queue == []:
#             break
#         sang_queue = []
#         fire_queue = []
#     if chk:
#         print(step)
#     else:
#         print('IMPOSSIBLE')














# 시간 초과
# T = int(input())
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# for test_case in range(T):
#     garo, sero = map(int, input().split())
#     building = [list(input()) for _ in range(sero)]
#     dummy_building = [building[i][:] for i in range(sero)]
#     chk = False
#     step = 1
#     while True:
#         cnt = 0
#         for i in range(sero):
#             for j in range(garo):
#                 if building[i][j] == '@':
#                     for k in range(4):
#                         if 0 <= i + dx[k] < sero and 0 <= j + dy[k] < garo and building[i + dx[k]][j + dy[k]] == '.':
#                             dummy_building[i + dx[k]][j + dy[k]] = '@'
#                 elif building[i][j] == '*':
#                     for k in range(4):
#                         if 0 <= i + dx[k] < sero and 0 <= j + dy[k] < garo and (building[i + dx[k]][j + dy[k]] == '.' or building[i + dx[k]][j + dy[k]] == '@'):
#                             dummy_building[i + dx[k]][j + dy[k]] = '*'
#         for i in range(sero):
#             for j in range(garo):
#                 if dummy_building[i][j] == '@' and building[i][j] == '.':
#                     building[i][j] = '@'
#                     cnt += 1
#                 elif dummy_building[i][j] == '*' and (building[i][j] == '.' or building[i][j] =='@'):
#                     building[i][j] = '*'
#         for i in range(sero):
#             if building[i][garo - 1] == '@' or building[i][0] == '@':
#                 chk = True
#         for i in range(garo):
#             if building[sero - 1][i] == '@' or building[0][i] == '@':
#                 chk = True
#         step += 1
#         if chk:
#             break
#         if cnt == 0:
#             break
#     if chk:
#         print(step)
#     else:
#         print('IMPOSSIBLE')

