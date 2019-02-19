import sys
sys.stdin = open('4861.txt', 'r')
sys.stdout = open('4861_out.txt', 'w')


def hoemun(a):
    n = len(a) >> 1
    for i in range(n):
        if a[i] != a[-(i + 1)]:
            return False
    return True


T = int(input())
for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    arr = [input() for _ in range(N)]
    chk = False
    ans = ''
    for i in range(N):
        for j in range(N - M + 1):
            if hoemun(arr[i][j: j + M]):
                ans = arr[i][j: j + M]
                chk = True
            elif hoemun(''.join([arr[k][i] for k in range(j, j + M)])):
                ans = ''.join([arr[k][i] for k in range(j, j + M)])
                chk = True
            if chk:
                break
        if chk:
            break
    print(f'#{test_case} {ans}')
