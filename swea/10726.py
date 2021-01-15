for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    answer = 'ON'
    for i in range(N):
        if (M >> 1) << 1 == M:
            answer = 'OFF'
            break
        M >>= 1
    print('#{} {}'.format(tc, answer))