# from time import time
# t = time()
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]
N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
geo = [[5]*N for _ in range(N)]
tree_cnt = [[0] * N for _ in range(N)]
tree = [[list() for _ in range(N)] for __ in range(N)]
for _ in range(M):
    x, y, year = map(int, input().split())
    tree[x - 1][y - 1].append(year)
    tree_cnt[x - 1][y - 1] += 1
for _ in range(K):
    for i in range(N):
        for j in range(N):
            for k in range(tree_cnt[i][j] - 1, -1, -1):
                if tree[i][j][k] <= geo[i][j]:
                    geo[i][j] -= tree[i][j][k]
                    tree[i][j][k] += 1
                else:
                    while k > -1:
                        geo[i][j] += tree[i][j].pop(k)//2
                        k -= 1
                        tree_cnt[i][j] -= 1
                    break
    for i in range(N):
        for j in range(N):
            for k in range(tree_cnt[i][j]):
                if tree[i][j][k] % 5 == 0:
                    for l in range(8):
                        x, y = i + dx[l], j + dy[l]
                        if 0 <= x < N and 0 <= y < N:
                            tree[x][y].append(1)
                            tree_cnt[x][y] += 1
    for i in range(N):
        for j in range(N):
            geo[i][j] += A[i][j]
ans = 0
for i in range(N):
    for j in range(N):
        ans += tree_cnt[i][j]
print(ans)
# print(time()-t)
# dx = [-1, 1, 0, 0, -1, 1, -1, 1]
# dy = [0, 0, -1, 1, -1, 1, 1, -1]
# N, M, K = map(int, input().split())
# A = [list(map(int, input().split())) for _ in range(N)]
# geo = [[5]*N for _ in range(N)]
# tree = list()
# dead_tree = list()
# dead = 0
# for _ in range(M):
#     x, y, year = map(int, input().split())
#     tree.append((x - 1, y - 1, year))
# for _ in range(K):
#     new_tree = list()
#     for __ in range(M):
#         x, y, year = tree.pop()
#         if year <= geo[x][y]:
#             geo[x][y] -= year
#             year += 1
#             tree.insert(0, (x, y, year))
#             if year % 5 == 0:
#                 for i in range(8):
#                     nx, ny = x + dx[i], y + dy[i]
#                     if 0 <= nx < N and 0 <= ny < N:
#                         new_tree.append((nx, ny, 1))
#                         M += 1
#         else:
#             dead_tree.append((x, y, year))
#             dead += 1
#             M -= 1
#     for __ in range(dead):
#         x, y, year = dead_tree.pop()
#         geo[x][y] += (year//2)
#     dead = 0
#     tree.extend(new_tree)
#     for i in range(N):
#         for j in range(N):
#             geo[i][j] += A[i][j]
# print(M)


# 재 채점으로 시간 초과가 되었다.
# from collections import deque
# X, Y, AGE, LIVE = 0, 1, 2, 3
# dx = [-1, 1, 0, 0, -1, 1, -1, 1]
# dy = [0, 0, -1, 1, -1, 1, 1, -1]
# N, M, K = map(int, input().split())
# A = [list(map(int, input().split())) for _ in range(N)]
# geo = [[5]*N for _ in range(N)]
# tree = {}
# dead_tree={}
# for i in range(N):
#     for j in range(N):
#         tree[(i, j)] = deque()
#         dead_tree[(i, j)] = deque()
# for _ in range(M):
#     a, b, c = map(int, input().split())
#     tree[(a - 1, b - 1)].append(c)
# for _ in range(K):
#     for i in range(N):
#         for j in range(N):
#             for k in range(len(tree[(i, j)])):
#                 temp = tree[(i, j)].pop()
#                 if temp <= geo[i][j]:
#                     geo[i][j] -= temp
#                     tree[(i, j)].appendleft(temp + 1)
#                 else:
#                     dead_tree[(i, j)].append(temp//2)
#                     M -= 1
#     for i in range(N):
#         for j in range(N):
#             for k in range(len(dead_tree[(i, j)])):
#                 geo[i][j] += dead_tree[(i, j)].pop()
#     for i in range(N):
#         for j in range(N):
#             for k in range(len(tree[(i, j)])):
#                 if tree[(i, j)][k] % 5 == 0:
#                     for l in range(8):
#                         x, y = i + dx[l], j + dy[l]
#                         if 0 <= x < N and 0 <= y < N:
#                             tree[(x, y)].append(1)
#                             M += 1
#     for i in range(N):
#         for j in range(N):
#             geo[i][j] += A[i][j]
# print(M)




# 시간 초과
# X, Y, AGE, LIVE = 0, 1, 2, 3
# dx = [-1, 1, 0, 0, -1, 1, -1, 1]
# dy = [0, 0, -1, 1, -1, 1, 1, -1]
# N, M, K = map(int, input().split())
# A = [list(map(int, input().split())) for _ in range(N)]
# geo = [[5]*N for _ in range(N)]
# tree = []
# for _ in range(M):
#     a, b, c = map(int, input().split())
#     tree.append([a - 1, b - 1, c, True])
# for _ in range(K):
#     for i in range(M - 1, -1, -1):
#         if geo[tree[i][X]][tree[i][Y]] >= tree[i][AGE]:
#             geo[tree[i][X]][tree[i][Y]] -= tree[i][AGE]
#             tree[i][AGE] += 1
#         else:
#             tree[i][LIVE] = False
#     for i in range(M - 1, -1, -1):
#         if tree[i][LIVE] == False:
#             geo[tree[i][X]][tree[i][Y]] += (tree[i][AGE] // 2)
#             del tree[i]
#             M -= 1
#     for i in range(M):
#         if tree[i][AGE] % 5 == 0:
#             for j in range(8):
#                 x, y = tree[i][X] + dx[j], tree[i][Y] + dy[j]
#                 if 0 <= x < N and 0 <= y < N:
#                     tree.append([x, y, 1, True])
#                     M += 1
#     for i in range(N):
#         for j in range(N):
#             geo[i][j] += A[i][j]
# print(M)