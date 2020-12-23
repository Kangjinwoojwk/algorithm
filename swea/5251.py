from queue import PriorityQueue
for tc in range(1, int(input()) + 1):
    N, E = map(int, input().split())
    edge=[[] for _ in range(N + 1)]
    visit = [True] * (N + 1)
    for _ in range(E):
        s, e, w = map(int, input().split())
        edge[s].append([e, w])
    Pq = PriorityQueue()
    Pq.put((0, 0))
    while True:
        w, s = Pq.get()
        visit[s] = False
        if visit[N] == False:
            break
        for i in edge[s]:
            if visit[i[0]]:
                Pq.put((w + i[1], i[0]))
    print('#{} {}'.format(tc, w))