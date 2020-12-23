import sys
sys.stdin = open('5108.txt', 'r')
sys.stdout = open('5108_out.txt', 'w')
T = int(input())
for test_case in range(1, T + 1):
    N, M, L = list(map(int, input().split()))
    li = list(map(int,input().split()))
    for _ in range(M):
        idx, num = list(map(int, input().split()))
        li = li[:idx] + [num] + li[idx:]
    print('#{} {}'.format(test_case, li[L]))
