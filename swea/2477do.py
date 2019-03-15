import sys
sys.stdin = open('2477.txt', 'r')
def sol(n):
    global ans, N, X
    pre = data[n][0]
    pre_cnt = 1
    for i in range(1, N):
        if pre == data[n][i]:
            pre_cnt += 1
        elif abs(pre - data[n][i]) > 1:
            break
        elif pre + 1 == data[n][i]:
            if pre_cnt >= X:
                pre = data[n][i]
                pre_cnt = 1
            else:
                break
        elif pre - 1 == data[n][i]:
            for j in range(1, X):
                if i + j == N or data[n][i] != data[n][i + j]:
                    break
            else:
                pre = data[n][i]
                pre_cnt = 1
            if pre != data[n][i]:
                break
    else:
        ans += 1
    pre = data[0][n]
    pre_cnt = 1
    for i in range(1, N):
        if pre == data[i][n]:
            pre_cnt += 1
        elif abs(pre - data[i][n]) > 1:
            break
        elif pre + 1 == data[i][n]:
            if pre_cnt >= X:
                pre = data[i][n]
                pre_cnt = 1
            else:
                break
        elif pre - 1 == data[i][n]:
            for j in range(1, X):
                if i + j == N or data[i][n] != data[i+j][n]:
                    break
            else:
                pre = data[i][n]
                pre_cnt = 1
            if pre != data[i][n]:
                break
    else:
        ans += 1

T = int(input())
for tc in range(1, T + 1):
    N, X = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        sol(i)
    print(ans)













# 슈웨이한 방법을 찾아 보자
# T = int(input())
# for tc in range(1, T + 1):
#     N, X = map(int, input().split())
#     data = [list(map(int, input().split())) for _ in range(N)]
#     ans = 0
#
#     for i in range(N):
#         garo_chk = True
#         sero_chk = True
#         garo_pre = data[i][0]
#         garo_pre_cnt = 1
#         sero_pre = data[0][i]
#         sero_pre_cnt = 1
#         for j in range(1, N):
#             if garo_chk:
#                 if garo_pre == data[i][j]:
#                     garo_pre_cnt += 1
#                 elif garo_pre != data[i][j]:
#                     if abs(data[i][j] - garo_pre) > 1:
#                         garo_chk = False
#                     elif data[i][j] > garo_pre:
#                         if garo_pre_cnt < X:
#                             garo_chk = False
#                         else:
#                             garo_pre = data[i][j]
#                             garo_pre_cnt = 1
#                     else:
#                         for k in range(1, X):
#                             if j + k < N and data[i][j + k] == data[i][j]:
#                                 continue
#                             else:
#                                 garo_chk = False
#                                 break
#                         else:
#                             garo_pre = data[i][j]
#                             garo_pre_cnt = 1
#             if sero_chk:
#                 if sero_pre == data[j][i]:
#                     sero_pre_cnt += 1
#                 elif sero_pre != data[j][i]:
#                     if abs(data[j][i] - sero_pre) > 1:
#                         sero_chk = False
#                     elif data[j][i] > sero_pre:
#                         if sero_pre_cnt < X:
#                             sero_chk = False
#                         else:
#                             sero_pre = data[j][i]
#                             sero_pre_cnt = 1
#                     else:
#                         for k in range(1, X):
#                             if j + k < N and data[j + k][i] == data[j][i]:
#                                 continue
#                             else:
#                                 sero_chk = False
#                                 break
#                         else:
#                             sero_pre = data[j][i]
#                             sero_pre_cnt = 1
#         if garo_chk:
#             ans += 1
#         if sero_chk:
#             ans += 1
#     print(ans)
