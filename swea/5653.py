import sys
sys.stdin = open('5653.txt', 'r')
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    di = {}
    for i in range(N):
        for j in range(M):
            if data[i][j]:
                di[(i, j)] = [data[i][j], 0]
    time = 0
    while time < K:
        new_di = {}
        for k, v in di.items():
            if time - v[1] == v[0]:
                for i in range(4):
                    x, y = k[0] + dx[i], k[1] + dy[i]
                    if (x, y) in new_di and new_di[(x, y)][0] < v[0]:
                        new_di[(x, y)][0] = v[0]
                    elif (x, y) not in di and (x, y) not in new_di:
                        new_di[(x, y)] = [v[0], time + 1]
        for k, v in new_di.items():
            di[k] = v
        time += 1
    ans = 0
    for v in di.values():
        if time - v[1] < 2 * v[0]:
            ans += 1
    print('#{} {}'.format(tc, ans))
