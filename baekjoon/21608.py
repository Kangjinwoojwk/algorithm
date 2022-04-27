dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
n = int(input())
position = [[0] * n for _ in range(n)]
data = list()
data_dict = dict()
position_score = [[0] * n for _ in range(n)]
answer = 0
for _ in range(n * n):
    num, s1, s2, s3, s4 = map(int, input().split())
    data.append([num, [s1, s2, s3, s4]])
    data_dict[num] = [s1, s2, s3, s4]
for _ in range(n * n):
    temp_student = data[0]
    data = data[1:]
    temp_point = [-1, -1, -1, -1]
    for x in range(n):
        for y in range(n):
            temp_like, temp_empty = 0, 0
            if position[x][y] == 0:
                for i in range(4):
                    if 0 <= x + dr[i] < n and 0 <= y + dc[i] < n:
                        if position[x + dr[i]][y + dc[i]] in temp_student[1]:
                            temp_like += 1
                        elif position[x + dr[i]][y + dc[i]] == 0:
                            temp_empty += 1
                if temp_like > temp_point[0]:
                    temp_point = [temp_like, temp_empty, x, y]
                elif temp_like == temp_point[0]:
                    if temp_empty > temp_point[1]:
                        temp_point = [temp_like, temp_empty, x, y]
    position[temp_point[2]][temp_point[3]] = temp_student[0]
for x in range(n):
    for y in range(n):
        for i in range(4):
            if 0 <= x + dr[i] < n and 0 <= y + dc[i] < n:
                if position[x + dr[i]][y + dc[i]] in data_dict[position[x][y]]:
                    position_score[x][y] += 1
for x in range(n):
    for y in range(n):
        if position_score == 1:
            answer += 1
        elif position_score == 2:
            answer += 10
        elif position_score == 3:
            answer += 100
        elif position_score == 4:
            answer += 1000
print(answer)



# dr = [1, 0, -1, 0]
# dc = [0, 1, 0, -1]
# n = int(input())
# position = [[0] * n for _ in range(n)]
# data = [list(map(int, input().split())) for _ in range(n * n)]
# data_dict = dict()
# answer = 0
# data_cnt = [[0] * n for _ in range(n)]
# for i in range(n * n):
#     temp_data = data[0]
#     data = data[1:]
#     temp_map = [[[0, 0]for _ in range(n)]for __ in range(n)]
#     for x in range(n):
#         for y in range(n):
#             if position[x][y] != 0:
#                 continue
#             for j in range(4):
#                 if 0 <= x + dr[j] < n and 0 <= y + dc[j] < n:
#                     if position[x + dr[j]][y + dc[j]] == 0:
#                         temp_map[x][y][1] += 1
#                     elif position[x + dr[j]][y + dc[j]] in temp_data[1:]:
#                         temp_map[x][y][0] += 1
#     check = [-1, -1]
#     check_point = [-1, -1]
#     for x in range(n):
#         for y in range(n):
#             if position[x][y] != 0:
#                 continue
#             elif check[0] < temp_map[x][y][0]:
#                 check = temp_map[x][y][:]
#                 check_point = [x, y]
#             elif check[0] == temp_map[x][y][0]:
#                 if check[1] < temp_map[x][y][1]:
#                     check = temp_map[x][y][:]
#                     check_point = [x, y]
#                 elif check[1] == temp_map[x][y][1]:
#                     if x < check_point[0]:
#                         check = temp_map[x][y][:]
#                         check_point = [x, y]
#                     elif x == check_point[0]:
#                         if y < check_point[1]:
#                             check = temp_map[x][y][:]
#                             check_point = [x, y]
#     position[check_point[0]][check_point[1]] = temp_data[0]
#     data_dict[temp_data[0]] = temp_data[1:]
# for x in range(3):
#     for y in range(3):
#         for j in range(4):
#             if 0 <= x + dr[j] < n and 0 <= y + dc[j] < n:
#                 if position[x + dr[j]][y + dc[j]] in data_dict[position[x][y]]:
#                     data_cnt[x][y] += 1
# for x in range(3):
#     for y in range(3):
#         if data_cnt[x][y] == 0:
#             continue
#         answer += 10 ** (data_cnt[x][y] - 1)
# print(answer)