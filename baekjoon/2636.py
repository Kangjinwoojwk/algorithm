dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def get_air(x, y):
    cheese[x][y] = 2
    for i in range(4):
        n_x, n_y = x + dx[i], y + dy[i]
        if cheese[n_x][n_y] == 0:
            get_air(n_x, n_y)
sero, garo = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(sero)]
for i in range(sero):
    cheese[i][0] = cheese[i][garo - 1] = 2
for i in range(garo):
    cheese[0][i] = cheese[sero - 1][i] = 2
queue = []
queue_start = queue_end = cnt = time = last = 0
while True:
    cnt = 0
    for i in range(queue_start, queue_end):
        cheese[queue[i][0]][queue[i][1]] = 2
    for i in range(1, sero - 1):
        for j in range(1, garo - 1):
            if cheese[i][j] == 0:
                for k in range(4):
                    x, y = i + dx[k], j + dy[k]
                    if 0 <= x < sero and 0 <= y < garo:
                        if cheese[x][y] == 2:
                            get_air(i, j)
                            break
    for i in range(1, sero - 1):
        for j in range(1, garo - 1):
            if cheese[i][j] == 1:
                for k in range(4):
                    x, y = i + dx[k], j + dy[k]
                    if 0 <= x < sero and 0 <= y < garo:
                        if cheese[x][y] == 2:
                            queue.append([i, j])
                            cnt += 1
                            break
    queue_start, queue_end = queue_end, queue_end + cnt

    if cnt == 0:
        break
    last = cnt
    time += 1
print(time)
print(last)







# 생각을 잘못했다. 이 방식이면 가운데 구멍이 있는곳도 바로 무너진다.
# while True:
#     for i in range(queue_start, queue_end):
#         cheese[queue[i][0]][queue[i][1]] = 0
#     for i in range(sero):
#         for j in range(garo):
#             if cheese[i][j] == 1:
#                 for k in range(4):
#                     x, y = i + dx[k], j + dy[k]
#                     if 0 <= x < sero and 0 <= y < garo:
#                         if cheese[x][y] == 0:
#                             queue.append([i, j])
#                             cnt += 1
#                             break
#     queue_start, queue_end = queue_end, queue_end + cnt
#     time += 1
#     if cnt == 0:
#         break
#     last = cnt