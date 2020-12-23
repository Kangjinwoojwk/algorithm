import sys
sys.stdin = open('2805.txt', 'r')
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, list(input()))) for i in range(N)]
    ans = 0
    i = 0
    j_start = j_end = N // 2
    while i < N:
        for j in range(j_start, j_end + 1):
            ans += data[i][j]
        if i < N // 2:
            j_start -= 1
            j_end += 1
        else:
            j_start += 1
            j_end -= 1
        i += 1
    print('#{} {}'.format(tc, ans))
