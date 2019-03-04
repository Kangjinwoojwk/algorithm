import sys
sys.stdin = open('5178.txt', 'r')
sys.stdout = open('5178_out.txt', 'w')
T = int(input())
for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())
    li = [0] * (N + 1)
    m = 1000
    for _ in range(M):
        node, value = map(int, input().split())
        li[node] = value
        if node < m:
            m = node
    m -= 1
    while m > 0:
        if 2 * m + 1 <= N:
            li[m] = li[2 * m] + li[2 * m + 1]
        else:
            li[m] = li[2 * m]
        m -= 1
    print('#{} {}'.format(test_case, li[L]))