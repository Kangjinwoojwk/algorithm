import sys
sys.stdin = open('1979.txt', 'r')
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        cnt_col = 0
        cnt_row = 0
        for j in range(N):
            if data[i][j] == 1:
                cnt_row += 1
            else:
                if cnt_row == K:
                    ans += 1
                cnt_row = 0
            if data[j][i] == 1:
                cnt_col += 1
            else:
                if cnt_col == K:
                    ans += 1
                cnt_col = 0
        else:
            if cnt_row == K:
                ans += 1
            if cnt_col == K:
                ans += 1
    print('#{} {}'.format(tc, ans))