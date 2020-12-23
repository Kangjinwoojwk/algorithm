from collections import deque
T = int(input())
for tc in range(1, T + 1):
    visit = [True] * 1000001
    N, M = map(int, input().split())
    Q = deque([N])
    visit[N] = False
    cnt = 0
    while visit[M]:
        cnt += 1
        for _ in range(len(Q)):
            x = Q.popleft()
            if x + 1 <= 1000000 and visit[x + 1]:
                visit[x + 1] = False
                Q.append(x + 1)
            if x - 1 >= 0 and visit[x - 1]:
                visit[x - 1] = False
                Q.append(x - 1)
            if x * 2 <= 1000000 and visit[x * 2]:
                visit[x * 2] = False
                Q.append(x * 2)
            if x - 10 >= 0 and visit[x - 10]:
                visit[x - 10] = False
                Q.append(x - 10)
    print('#{} {}'.format(tc, cnt))