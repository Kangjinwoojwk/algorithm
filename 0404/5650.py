for tc in range(1, int(input()) + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            if data[i][j] == 0:
                for k in range(4):
                    Q = [(i, j, k)]
                    cnt = 0
                    while Q:
                        x, y, direction = Q.pop()


    print('#{} {}'.format(tc, ans))