import sys
sys.stdin = open('2115.txt', 'r')
sys.stdout = open('2115_out.txt', 'w')
def get(li, C):
    n = len(li)
    max_honey = 0
    for i in range(1 << n):
        cnt = 0
        honey = 0
        for j in range(n):
            if 1 << j & i:
                if cnt + li[j] <= C:
                    cnt += li[j]
                    honey += li[j] ** 2
                    if honey > max_honey:
                        max_honey = honey
    return max_honey
def max_honey(N, M):
    max_value = 0
    for i in range(N):
        for j in range(N - M + 1):
            for k in range(i, N):
                for l in range(N - M + 1):
                    if i == k and l < j + M:
                        continue
                    h = honey[i][j] + honey[k][l]
                    if h > max_value:
                        max_value = h
    return max_value
T = int(input())
for test_case in range(1, T + 1):
    N, M, C = map(int, input().split())
    hive = [list(map(int, input().split())) for _ in range(N)]
    honey = [[0] * (N - M + 1) for _ in range(N)]
    for i in range(N):
        for j in range(N - M + 1):
            honey[i][j] = get(hive[i][j:j + M], C)
    print('#{} {}'.format(test_case, max_honey(N, M)))

