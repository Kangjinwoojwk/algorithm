import sys
sys.stdin = open('4014.txt', 'r')
def sol(n):
    global N, X, ans
    pre = data[n][0]
    cnt = 1
    i = 1
    while i < N:
        if data[n][i] == pre:
            cnt += 1
        else:
            if abs(data[n][i] - pre) > 1:
                break
            else:
                if data[n][i] > pre:
                    if cnt >= X:
                        pre = data[n][i]
                        cnt = 1
                    else:
                        break
                else:
                    for j in range(1, X):
                        if i + j < N and data[n][i] == data[n][i + j]:
                            continue
                        else:
                            break
                    else:
                        i += X - 1
                        pre = data[n][i]
                        cnt = 0
                    if pre != data[n][i]:
                        break
        i += 1
    else:
        ans += 1
    pre = data[0][n]
    cnt = 1
    i = 1
    while i < N:
        if data[i][n] == pre:
            cnt += 1
        else:
            if abs(data[i][n] - pre) > 1:
                break
            else:
                if data[i][n] > pre:
                    if cnt >= X:
                        pre = data[i][n]
                        cnt = 1
                    else:
                        break
                else:
                    for j in range(1, X):
                        if i + j < N and data[i][n] == data[i + j][n]:
                            continue
                        else:
                            break
                    else:
                        i += X - 1
                        pre = data[i][n]
                        cnt = 0
                    if pre != data[i][n]:
                        break
        i += 1
    else:
        ans += 1

T = int(input())
for tc in range(1, T + 1):
    N, X = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        sol(i)
    print('#{} {}'.format(tc, ans))
