from collections import deque
for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    visit = [True] * (N + 1)
    edge = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        edge[a].append(b)
        edge[b].append(a)
    Q = deque()
    Q.append(1)
    visit[1] = False
    for i in range(2):
        for j in range(len(Q)):
            a = Q.popleft()
            for k in edge[a]:
                if visit[k]:
                    visit[k] = False
                    Q.append(k)
    print('#{} {}'.format(tc, visit.count(False) - 1))