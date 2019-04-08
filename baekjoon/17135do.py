




# from collections import deque
# dx = [0, -1, 0]
# dy = [-1, 0, 1]
# def simulate():
#     global ans
#     kill = list()
#     for i in range(N):
#         Q = [deque() for _ in range(3)]
#         for j in range(3):
#             Q[j].append((N - i - 1, archor[j]))
#         dead = set()
#         for j in range(3):
#             for k in range(D):
#                 for l in range(len(Q[j])):
#                     x, y = Q[j].popleft()
#                     if data[x][y] == 1:
#                         dead.add((x, y))
#                         break
#                     for m in range(3):
#                         nx, ny = x + dx[m], y + dy[m]
#                         if 0 <= nx < N and 0 <= ny < M:
#                             Q[j].append((nx, ny))
#         for j in dead:
#             kill.append(j)
#             data[j[0]][j[1]] = 0
#     if len(kill) > ans:
#         ans = len(kill)
#     for i in kill:
#         data[i[0]][i[1]] = 1
# def sol(n, cnt):
#     if cnt == 0:
#         simulate()
#         return
#     if n == M:
#         return
#     sol(n + 1, cnt)
#     archor.append(n)
#     sol(n + 1, cnt - 1)
#     archor.pop()
# N, M, D = map(int, input().split())
# data = [list(map(int, input().split()))for _ in range(N)]
# archor = list()
# ans = 0
# sol(0, 3)
# print(ans)

# from collections import deque
# dx = [0, -1, 0]
# dy = [-1, 0, 1]
# def simulation():
#     global ans
#     temp = [data[_][:] for _ in range(N)]
#     cnt = 0
#     for i in range(N):
#         Q = [deque() for _ in range(3)]
#         for j in range(3):
#             Q[j].append((N - i - 1, archor[j]))
#         kill = set()
#         for j in range(3):
#             for k in range(D):
#                 visit = [[True] * M for i in range(N)]
#                 for m in range(len(Q[j])):
#                     x, y = Q[j].popleft()
#                     if temp[x][y] == 1:
#                         kill.add((x, y))
#                         break
#                     for l in range(3):
#                         nx, ny = x + dx[l], y + dy[l]
#                         if 0 <= nx < N and 0 <= ny < M:
#                             if visit[nx][ny]:
#                                 visit[nx][ny] = False
#                                 Q[j].append((nx, ny))
#         cnt += len(kill)
#         for j in kill:
#             temp[j[0]][j[1]] = 0
#     if cnt > ans:
#         ans = cnt
#
# def sol(n, cnt):
#     if cnt == 0:
#         simulation()
#         return
#     if n == M:
#         return
#     archor.append(n)
#     sol(n + 1, cnt - 1)
#     archor.pop()
#     sol(n + 1, cnt)
# N, M, D = map(int, input().split())
# data = [list(map(int, input().split())) for _ in range(N)]
# archor = list()
# ans = 0
# sol(0, 3)
# print(ans)