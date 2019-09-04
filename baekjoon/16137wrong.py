dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
move = [[10000] * N for _ in range(N)]
use = [[True] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if data[i][j] != 1:
            if (i - 1 >= 0 and data[i - 1][j] != 1) or (i + 1 < N and data[i + 1][j] != 1):
                if (j - 1 >= 0 and data[i][j - 1] != 1) or (j + 1 < N and data[i][j + 1] != 1):
                    use[i][j] = False
for i in range(N):
    for j in range(N):
        if not use[i][j]:
            for k in range(4):
                for l in range(1, N):
                    if 0 <= i + dx[k] * l < N and 0 <= j + dy[k] * l < N:
                        if not use[i + dx[k] * l][j + dy[k] * l]:
                            break
                        if data[i + dx[k] * l][j + dy[k] * l] > 1:
                            for m in range(1, N):
                                if not use[i + dx[k] * m][j + dy[k] * m] or not (0 <= i + dx[k] * m < N and 0 <= j + dy[k] * m < N) :
                                    break
                                else:
                                    use[i + dx[k] * m][j + dy[k] * m] = False
                    else:
                        break
queue = [(0, 0, 0, 1)]
move[0][0] = 0
ans = 0
while move[N - 1][N - 1] == 10000:
    ans, x, y, bridge = queue.pop(0)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if data[nx][ny] == 1 and move[nx][ny] == 10000:
                move[nx][ny] = ans + 1
                for j in range(len(queue)):
                    if (ans + 1, nx, ny, bridge) < queue[j]:
                        queue.insert(j, (ans + 1, nx, ny, bridge))
                        break
                else:
                    queue.append((ans + 1, nx, ny, bridge))
            elif data[nx][ny] > 1 and move[nx][ny] == 10000:
                move[nx][ny] = (ans // data[nx][ny] + 1) * data[nx][ny]
                for j in range(len(queue)):
                    if (((ans // data[nx][ny]) + 1) * data[nx][ny], nx, ny, bridge) < queue[j]:
                        queue.insert(j, (((ans // data[nx][ny]) + 1) * data[nx][ny], nx, ny, bridge))
                        break
                else:
                    queue.append((((ans // data[nx][ny]) + 1) * data[nx][ny], nx, ny, bridge))
            elif move[nx][ny] == 10000:
                if data[x][y] == 1 and bridge == 1 and use[nx][ny]:
                    move[nx][ny] = ((ans // M) + 1) * M
                    for j in range(len(queue)):
                        if (((ans // M) + 1) * M, nx, ny, bridge - 1) < queue[j]:
                            queue.insert(j, (((ans // M) + 1) * M, nx, ny, bridge - 1))
                            break
                    else:
                        queue.append((((ans // M) + 1) * M, nx, ny, bridge - 1))
print(move[N - 1][N - 1])

# dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
# N, M = map(int, input().split())
# data = [list(map(int, input().split())) for _ in range(N)]
# move = [[5000] * N for _ in range(N)]
# use = [[True] * N for _ in range(N)]
# for i in range(N):
#     for j in range(N):
#         if data[i][j] != 1:
#             if (i - 1 >= 0 and data[i - 1][j] != 1) or (i + 1 < N and data[i + 1][j] != 1):
#                 if (j - 1 >= 0 and data[i][j - 1] != 1) or (j + 1 < N and data[i][j + 1] != 1):
#                     use[i][j] = False
# for i in range(N):
#     for j in range(N):
#         if not use[i][j]:
#             for k in range(4):
#                 for l in range(1, N):
#                     if 0 <= i + dx[k] * l < N and 0 <= j + dy[k] * l < N:
#                         if not use[i + dx[k] * l][j + dy[k] * l]:
#                             break
#                         if data[i + dx[k] * l][j + dy[k] * l] > 1:
#                             for m in range(1, N):
#                                 if not use[i + dx[k] * m][j + dy[k] * m] or not (0 <= i + dx[k] * m < N and 0 <= j + dy[k] * m < N) :
#                                     break
#                                 else:
#                                     use[i + dx[k] * m][j + dy[k] * m] = False
#                     else:
#                         break
# queue = [(0, 0)]
# move[0][0] = 0
# while queue:
#     x, y = queue.pop(0)
#     for i in range(4):
#         nx, ny = x + dx[i], y + dy[i]
#         if 0 <= nx < N and 0 <= ny < N:
#             if data[nx][ny] == 1:
#                 if move[nx][ny] >= move[x][y] + 1:
#                     move[nx][ny] = move[x][y] + 1
#                     queue.append((nx, ny))
#             elif data[nx][ny] > 1 and data[x][y] == 1:
#                 if move[nx][ny] >= ((move[x][y] // data[nx][ny]) + 1) * data[nx][ny]:
#                     move[nx][ny] = ((move[x][y] // data[nx][ny]) + 1) * data[nx][ny]
#                     queue.append((nx, ny))
#             else:
#                 if data[x][y] == 1:
#                     if use[nx][ny]:
#                         if move[nx][ny] > ((move[x][y] // M) + 1) * M:
#                             move[nx][ny] = ((move[x][y] // M) + 1) * M
#                             queue.append((nx, ny))
# print(move[N - 1][N - 1])



# dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
# N, M = map(int, input().split())
# data = [list(map(int, input().split())) for _ in range(N)]
# move = [[[5000] * N for _ in range(N)] for __ in range(2)]
# use = [[True] * N for _ in range(N)]
# for i in range(N):
#     for j in range(N):
#         if data[i][j] != 1:
#             if (i - 1 >= 0 and data[i - 1][j] != 1) or (i + 1 < N and data[i + 1][j] != 1):
#                 if (j - 1 >= 0 and data[i][j - 1] != 1) or (j + 1 < N and data[i][j + 1] != 1):
#                     use[i][j] = False
# for i in range(N):
#     for j in range(N):
#         if not use[i][j]:
#             for k in range(4):
#                 for l in range(1, N):
#                     if 0 <= i + dx[k] * l < N and 0 <= j + dy[k] * l < N:
#                         if not use[i + dx[k] * l][j + dy[k] * l]:
#                             break
#                         if data[i + dx[k] * l][j + dy[k] * l] > 1:
#                             for m in range(1, N):
#                                 if not use[i + dx[k] * m][j + dy[k] * m] or not (0 <= i + dx[k] * m < N and 0 <= j + dy[k] * m < N) :
#                                     break
#                                 else:
#                                     use[i + dx[k] * m][j + dy[k] * m] = False
#                     else:
#                         break
# queue = [(0, 0, 0)]
# move[0][0][0] = 0
# while queue:
#     x, y, pan = queue.pop(0)
#     for i in range(4):
#         nx, ny = x + dx[i], y + dy[i]
#         if 0 <= nx < N and 0 <= ny < N:
#             if data[nx][ny] == 1:
#                 if move[pan][nx][ny] >= move[pan][x][y] + 1:
#                     move[pan][nx][ny] = move[pan][x][y] + 1
#                     queue.append((nx, ny, pan))
#             elif data[nx][ny] > 1 and data[x][y] == 1:
#                 if move[pan][nx][ny] >= ((move[pan][x][y] // data[nx][ny]) + 1) * data[nx][ny]:
#                     move[pan][nx][ny] = ((move[pan][x][y] // data[nx][ny]) + 1) * data[nx][ny]
#                     queue.append((nx, ny, pan))
#             else:
#                 if data[x][y] == 1:
#                     if pan == 0 and use[nx][ny]:
#                         if move[pan + 1][nx][ny] >= ((move[pan][x][y] // M) + 1) * M:
#                             move[pan + 1][nx][ny] = ((move[pan][x][y] // M) + 1) * M
#                             queue.append((nx, ny, pan + 1))
# print(min(move[0][N - 1][N - 1], move[1][N - 1][N - 1]))