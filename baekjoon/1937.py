import sys
sys.setrecursionlimit(500000)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def sol(x, y):
    if visit[x][y]:
        return visit[x][y]
    get = list()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and data[nx][ny] > data[x][y]:
            get.append(sol(nx, ny))
    if get:
        visit[x][y] = max(get) + 1
    else:
        visit[x][y] = 1
    return visit[x][y]


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visit[i][j] == 0:
            visit[i][j] = sol(i, j)
ans = 0
for i in range(N):
    for j in range(N):
        if visit[i][j] > ans:
            ans = visit[i][j]
print(ans)



# BFS도 시간 초과
# from collections import deque
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# def sol(x, y):
#     global ans
#     que = deque()
#     que.append((x, y))
#     cnt = 0
#     while que:
#         cnt += 1
#         for i in range(len(que)):
#             x, y = que.popleft()
#             for j in range(4):
#                 nx, ny = x + dx[j], y + dy[j]
#                 if 0 <= nx < N and 0 <= ny < N:
#                     if data[nx][ny] > data[x][y]:
#                         visit[nx][ny] = False
#                         que.append((nx, ny))
#     if cnt > ans:
#         ans = cnt
#
# N = int(input())
# data = [list(map(int, input().split())) for _ in range(N)]
# visit = [[True] * N for _ in range(N)]
# ans = 0
# for i in range(N):
#     for j in range(N):
#         if visit[i][j]:
#             sol(i, j)
# print(ans)

# 하아...시간 초과... 연산 줄이려고 visit을 썼지만 시간 초과
# import sys
# sys.setrecursionlimit(30000)
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# def sol(x, y, cnt):
#     global ans
#     if cnt > ans:
#         ans = cnt
#     for i in range(4):
#         nx, ny = x + dx[i], y + dy[i]
#         if 0 <= nx < N and 0 <= ny < N:
#             if data[nx][ny] > data[x][y]:
#                 visit[nx][ny] = False
#                 sol(nx, ny, cnt + 1)
# N = int(input())
# data = [list(map(int, input().split())) for _ in range(N)]
# visit = [[True] * N for _ in range(N)]
# ans = 0
# for i in range(N):
#     for j in range(N):
#         if visit[i][j]:
#             sol(i, j, 1)
# print(ans)