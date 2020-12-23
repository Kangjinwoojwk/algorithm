import sys
sys.stdin = open('5102.txt', 'r')
sys.stdout = open('5102_out.txt', 'w')
# 도착 못하는 경우 0 출력
T = int(input())
for test_case in range(1, T + 1):
    V, E = list(map(int, input().split()))
    Node = [list(map(int, input().split()))for _ in range(E)]
    edge = [[] for _ in range(V + 1)]
    for i in Node:
        edge[i[0]].append(i[1])
        edge[i[1]].append(i[0])
    S, G = list(map(int, input().split()))
    not_visited = [True] * (V + 1)
    queue = []
    queue.append(S)
    not_visited[S] = False
    step = 0
    start = 0
    end = 1
    while not_visited[G]:
        cnt = 0
        end = len(queue)
        for i in range(start, end):
            for j in edge[queue[i]]:
                if not_visited[j]:
                    queue.append(j)
        start = end
        for i in queue:
            if not_visited[i]:
                not_visited[i] = False
                cnt += 1
        if cnt == 0:
            break
        step += 1
    if not_visited[G]:
        step = 0
    print('#{} {}'.format(test_case, step))


