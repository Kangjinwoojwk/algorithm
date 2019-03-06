dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, M = map(int, input().split())
input_map = [list(input()) for _ in range(N)]
visit = [[[False] * M for _ in range(N)] for __ in range(2)]
visit[0][0][0] = visit[1][0][0] = True
queue = [[0, 0, 1]]
que_start = 0
que_end = 1
ans = -1
step = 1
while ans == -1:
    que_cnt = 0
    for i in range(que_start, que_end):
        if queue[i][0] == N - 1 and queue[i][1] == M - 1:
            ans = step
            break
        for j in range(4):
            x, y = queue[i][0] + dx[j], queue[i][1] + dy[j]
            if x < 0 or y < 0 or x >= N or y >= M:
                continue
            if visit[queue[i][2]][x][y]:
                continue
            if input_map[x][y] == '1' and queue[i][2] == 0:
                continue
            if input_map[x][y] == '0':
                if queue[i][2] == 1:
                    visit[0][x][y] = True
                visit[queue[i][2]][x][y] = True
                queue.append([x, y, queue[i][2]])
                que_cnt += 1
            if input_map[x][y] == '1' and queue[i][2] == 1:
                visit[0][x][y] = True
                queue.append([x, y, 0])
                que_cnt += 1
    if que_cnt == 0:
        break
    que_start, que_end = que_end, que_end + que_cnt
    step += 1
print(ans)



    






# dfs로 풀었다. 시간 초과도 아니고 런타임 에러라고 한다.
# ....?어디서 잘못 된거지....
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# def sol(x, y, step, wall):
#     global N, M, ans
#     if x == N - 1 and y == M - 1:
#         if ans == -1 or ans > step:
#             ans = step
#     for i in range(4):
#         next_x, next_y = x + dx[i], y + dy[i]
#         if 0 > next_x or 0 > next_y or next_x == N or next_y == M:
#             continue
#         if visit[next_x][next_y]:
#             continue
#         if input_map[next_x][next_y] == '1' and wall == 0:
#             continue
#         if input_map[next_x][next_y] == '1' and wall > 0:
#             visit[next_x][next_y] = True
#             sol(next_x, next_y, step + 1, wall - 1)
#             visit[next_x][next_y] = False
#         if input_map[next_x][next_y] == '0':
#             visit[next_x][next_y] = True
#             sol(next_x, next_y, step + 1, wall)
#             visit[next_x][next_y] = False
# N, M = map(int, input().split())
# input_map = [list(input()) for _ in range(N)]
# visit = [[False] * M for _ in range(N)]
# ans = -1
# visit[0][0] = True
# sol(0, 0, 1, 1)
# print(ans)
