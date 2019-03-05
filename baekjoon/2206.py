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
