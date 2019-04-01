for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    got = [0] * N
    max_get = 0
    for i in range(M):
        for j in range(N):
            if B[i] >= A[j]:
                got[j] += 1
                break
    print('#{} {}'.format(tc, got.index(max(got)) + 1))