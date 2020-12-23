from collections import deque
for tc in range(1, int(input()) + 1):
    N = int(input())
    score = list(map(int, input().split()))
    score.sort()
    visit = [True] * 10001
    Q = deque()
    Q.append(0)
    visit[0] = False
    n = 0
    while n < N:
        for _ in range(len(Q)):
            sc = Q.popleft()
            Q.append(sc)
            sc += score[n]
            if visit[sc]:
                visit[sc] = False
                Q.append(sc)
        n += 1
    print('#{} {}'.format(tc, visit.count(False)))