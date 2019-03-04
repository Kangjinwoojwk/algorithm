import sys
sys.stdin = open('5120.txt', 'r')
sys.stdout = open('5120_out.txt', 'w')
T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    li = list(map(int, input().split()))
    ptr = 0
    for _ in range(K):
        ptr += M
        if ptr == N:
            li.append(li[-1]+li[0])
        else:
            ptr %= N
            li = li[:ptr] + [li[ptr - 1] + li[ptr]] + li[ptr:]
        N += 1
    print('#{}'.format(test_case), end='')
    i = 0
    while N > 0 and i < 10:
        print(' {}'.format(li[N - 1]), end='')
        N -= 1
        i += 1
    print()
