import sys
sys.stdin = open('4869.txt', 'r')
sys.stdout = open('4869_out.txt', 'w')


def sol(N):
    if memo[N] != 0:
        return memo[N]
    elif N <= 1:
        return 1
    else:
        memo[N] = sol(N-1) + sol(N-2) + sol(N-2)
        return memo[N]


T = int(input())
memo = [0] * 31
memo[1] = 1
for test_case in range(1, T + 1):
    N = int(input()) // 10
    ans = sol(N)
    print(f'#{test_case} {ans}')
