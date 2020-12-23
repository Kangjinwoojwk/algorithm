import sys
sys.stdin = open('1974.txt', 'r')
T = int(input())
for tc in range(1, T + 1):
    ans = 1
    data = [list(map(int, input().split())) for _ in range(9)]
    chk = [True]*10
    chk[0] = False
    for i in range(9):
        for j in range(1, 10):
            chk[j] = True
        for j in range(9):
            chk[data[i][j]] = False
        for j in range(1, 10):
            if chk[j]:
                ans = 0
    if ans == 1:
        for i in range(9):
            for j in range(1, 10):
                chk[j] = True
            for j in range(9):
                chk[data[j][i]] = False
            for j in range(1, 10):
                if chk[j]:
                    ans = 0
    if ans == 1:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                for k in range(1, 10):
                    chk[k] = True
                for k in range(3):
                    for l in range(3):
                        chk[data[i + k][j + l]] = False
                for k in range(1, 10):
                    if chk[k]:
                        ans = 0
    print('#{} {}'.format(tc, ans))