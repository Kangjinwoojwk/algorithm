from collections import deque
X, Y, AGE, LIVE = 0, 1, 2, 3
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]
N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
geo = [[5]*N for _ in range(N)]
tree = {}
dead_tree={}
for i in range(N):
    for j in range(N):
        tree[(i, j)] = deque()
        dead_tree[(i, j)] = deque()
for _ in range(M):
    a, b, c = map(int, input().split())
    tree[(a - 1, b - 1)].append(c)
for _ in range(K):
    for i in range(N):
        for j in range(N):
            for k in range(len(tree[(i, j)])):
                temp = tree[(i, j)].pop()
                if temp <= geo[i][j]:
                    geo[i][j] -= temp
                    tree[(i, j)].appendleft(temp + 1)
                else:
                    dead_tree[(i, j)].append(temp//2)
                    M -= 1
    for i in range(N):
        for j in range(N):
            for k in range(len(dead_tree[(i, j)])):
                geo[i][j] += dead_tree[(i, j)].pop()
    for i in range(N):
        for j in range(N):
            for k in range(len(tree[(i, j)])):
                if tree[(i, j)][k] % 5 == 0:
                    for l in range(8):
                        x, y = i + dx[l], j + dy[l]
                        if 0 <= x < N and 0 <= y < N:
                            tree[(x, y)].append(1)
                            M += 1
    for i in range(N):
        for j in range(N):
            geo[i][j] += A[i][j]
print(M)




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