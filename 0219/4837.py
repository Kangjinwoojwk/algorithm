import sys
sys.stdin = open('4837.txt', 'r')
sys.stdout = open('4837_out.txt', 'w')


def sol(N, K, cnt, ptr, chk, ans):
    if N == cnt:
        sum_v = 0
        i = 1
        while i < 13:
            if chk[i]:
                sum_v += i
            i += 1
        if sum_v == K:
            ans[0] += 1
        return
    elif ptr > 12:
        return
    else:
        chk[ptr] = True
        sol(N, K, cnt + 1, ptr + 1, chk, ans)
        chk[ptr] = False
        sol(N, K, cnt, ptr + 1, chk, ans)


T = int(input())
for test_case in range(1, T + 1):
    N, K = list(map(int, input().split()))
    chk = [False] * 13
    ans = [0]
    sol(N, K, 0, 1, chk, ans)
    print(f'#{test_case} {ans[0]}')
