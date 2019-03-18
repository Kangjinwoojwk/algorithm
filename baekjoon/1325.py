from collections import deque
N, M = map(int, input().split())
li = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    li[b].append(a)
ans = []
max_v = 0
for i in range(1, N + 1):
    Q = deque()
    visit = [True] * (N + 1)
    visit[i] = False
    Q.append(i)
    while Q:
        for j in range(len(Q)):
            temp = Q.popleft()
            for k in li[temp]:
                if visit[k]:
                    visit[k] = False
                    Q.append(k)
    cnt = visit.count(False)
    if cnt > max_v:
        max_v = cnt
        ans = [i]
    elif cnt == max_v:
        ans.append(i)
print(' '.join(map(str, ans)))


# 시간 초과
# N, M = map(int, input().split())
# li = [[]for _ in range(N +1)]
# for i in range(M):
#     a, b = map(int, input().split())
#     li[b].append(a)
# ans = 0
# an = []
# for i in range(1, N + 1):
#     que = [i]
#     visit = [True] * (N + 1)
#     visit[i] = False
#     while que:
#         temp = que.pop(0)
#         for j in li[temp]:
#             if visit[j]:
#                 visit[j] = False
#                 que.append(j)
#     cnt = visit.count(False)
#     if cnt > ans:
#         ans = cnt
#         an = [i]
#     elif cnt == ans:
#         an.append(i)
# print(' '.join(map(str,an)))