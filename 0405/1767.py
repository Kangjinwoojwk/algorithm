import sys
sys.stdin = open('1767.txt','r')
def sol(n, connect, line_lenth):
    global N, ans, max_connect, processor_cnt
    if processor_cnt == n:
        if max_connect < connect:
            max_connect = connect
            ans = line_lenth
        elif max_connect == connect and ans > line_lenth:
            ans = line_lenth
        return
    for direction in range(4):
        if direction == 0:
            if sum([board[k][processor[n][1]] for k in range(processor[n][0])]) == 0:
                for l in range(processor[n][0]):
                    board[l][processor[n][1]] = 1
                sol(n + 1, connect + 1, line_lenth + processor[n][0])
                for l in range(processor[n][0]):
                    board[l][processor[n][1]] = 0
        elif direction == 1:
            if sum(board[processor[n][0]][processor[n][1] + 1:]) == 0:
                for l in range(processor[n][1] + 1, N):
                    board[processor[n][0]][l] = 1
                sol(n + 1, connect + 1, line_lenth + N - 1 - processor[n][1])
                for l in range(processor[n][1] + 1, N):
                    board[processor[n][0]][l] = 0
        elif direction == 2:
            if sum([board[k][processor[n][1]] for k in range(processor[n][0] + 1, N)]) == 0:
                for l in range(processor[n][0] + 1, N):
                    board[l][processor[n][1]] = 1
                sol(n + 1, connect + 1, line_lenth + N - 1 - processor[n][0])
                for l in range(processor[n][0] + 1, N):
                    board[l][processor[n][1]] = 0
        elif direction == 3:
            if sum(board[processor[n][0]][:processor[n][1]]) == 0:
                for l in range(processor[n][1]):
                    board[processor[n][0]][l] = 1
                sol(n + 1, connect + 1, line_lenth + processor[n][1])
                for l in range(processor[n][1]):
                    board[processor[n][0]][l] = 0
    sol(n + 1, connect, line_lenth)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    ans = 1 << 30
    max_connect = 0
    processor_cnt = 0
    processor = []
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if board[i][j] == 1:
                processor_cnt += 1
                processor.append([i, j])
    sol(0, 0, 0)
    print('#{} {}'.format(test_case, ans))



# 이 방식은 뭔가 잘못 됐다. 디버깅 보다 새로 짜는게 덜 복잡 할 것 같다.
# def sol(n, line_lenth, connect):
#     global N, ans, max_connect, processor_cnt
#     if n == processor_cnt:
#         if max_connect < connect:
#             max_connect = connect
#             ans = line_lenth
#         elif max_connect == connect and ans > line_lenth:
#             ans = line_lenth
#         return
#     for i in range(4):
#         if i == 0:
#             for j in range(1, N):
#                 if processor[n][0] - j == -1:
#                     line_lenth += (j - 1)
#                     connect += 1
#                     for k in range(1, j):
#                         board[processor[n][0] - k][processor[n][1]] = 1
#                     sol(n + 1, line_lenth, connect)
#                     for k in range(1, j):
#                         board[processor[n][0] - k][processor[n][1]] = 0
#                     connect -= 1
#                     line_lenth -= (j - 1)
#                     break
#                 if board[processor[n][0] - j][processor[n][1]] == 0:
#                     pass
#                 if board[processor[n][0] - j][processor[n][1]] == 1:
#                     break
#         elif i == 1:
#             for j in range(1, N):
#                 if processor[n][1] + j == N:
#                     line_lenth += (j - 1)
#                     connect += 1
#                     for k in range(1, j):
#                         board[processor[n][0]][processor[n][1] + k] = 1
#                     sol(n + 1, line_lenth, connect)
#                     for k in range(1, j):
#                         board[processor[n][0]][processor[n][1] + k] = 0
#                     connect -= 1
#                     line_lenth -= (j - 1)
#                     break
#                 if board[processor[n][0]][processor[n][1] + j] == 0:
#                     pass
#                 if board[processor[n][0]][processor[n][1] + j] == 1:
#                     break
#         elif i == 2:
#             for j in range(1, N):
#                 if processor[n][0] + j == N:
#                     line_lenth += (j - 1)
#                     connect += 1
#                     for k in range(1, j):
#                         board[processor[n][0] + k][processor[n][1]] = 1
#                     sol(n + 1, line_lenth, connect)
#                     for k in range(1, j):
#                         board[processor[n][0] + k][processor[n][1]] = 0
#                     connect -= 1
#                     line_lenth -= (j - 1)
#                     break
#                 if board[processor[n][0] + j][processor[n][1]] == 0:
#                     pass
#                 if board[processor[n][0] + j][processor[n][1]] == 1:
#                     break
#         elif i == 3:
#             for j in range(1, N):
#                 if processor[n][1] - j == N:
#                     line_lenth += (j - 1)
#                     connect += 1
#                     for k in range(1, j):
#                         board[processor[n][0]][processor[n][1] - k] = 1
#                     sol(n + 1, line_lenth, connect)
#                     for k in range(1, j):
#                         board[processor[n][0]][processor[n][1] - k] = 0
#                     connect -= 1
#                     line_lenth -= (j - 1)
#                     break
#                 if board[processor[n][0]][processor[n][1] - j] == 0:
#                     pass
#                 if board[processor[n][0]][processor[n][1] - j] == 1:
#                     break
#     sol(n + 1, line_lenth, connect)





# 조합은 망했다
# def cal_line_lenth():
#     global processor_cnt, N, max_connect, ans
#     connect = 0
#     line_lenth = 0
#     instant_board = [board[i][:] for i in range(N)]
#     for i in range(processor_cnt):
#         if processor[i][2] == 0:
#             for j in range(1, N):
#                 if processor[i][0] - j == -1:
#                     line_lenth += j - 1
#                     connect += 1
#                     for k in range(j):
#                         instant_board[processor[i][0] - k][processor[i][1]] = 1
#                     break
#                 if instant_board[processor[i][0] - j][processor[i][1]] == 0:
#                     pass
#                 if instant_board[processor[i][0] - j][processor[i][1]] == 1:
#                     break
#         elif processor[i][2] == 1:
#             for j in range(1, N):
#                 if processor[i][1] + j == N:
#                     line_lenth += j - 1
#                     connect += 1
#                     for k in range(j):
#                         instant_board[processor[i][0]][processor[i][1] + k] = 1
#                     break
#                 if instant_board[processor[i][0]][processor[i][1] + j] == 0:
#                     pass
#                 if instant_board[processor[i][0]][processor[i][1] + j] == 1:
#                     break
#         elif processor[i][2] == 2:
#             for j in range(1, N):
#                 if processor[i][0] + j == N:
#                     line_lenth += j - 1
#                     connect += 1
#                     for k in range(j):
#                         instant_board[processor[i][0] + k][processor[i][1]] = 1
#                     break
#                 if instant_board[processor[i][0] + j][processor[i][1]] == 0:
#                     pass
#                 if instant_board[processor[i][0] + j][processor[i][1]] == 1:
#                     break
#         elif processor[i][2] == 3:
#             for j in range(1, N):
#                 if processor[i][1] - j == -1:
#                     line_lenth += j - 1
#                     connect += 1
#                     for k in range(j):
#                         instant_board[processor[i][0]][processor[i][1] - k] = 1
#                     break
#                 if instant_board[processor[i][0]][processor[i][1] - j] == 0:
#                     pass
#                 if instant_board[processor[i][0]][processor[i][1] - j] == 1:
#                     break
#     if connect > max_connect:
#         max_connect = connect
#         ans = line_lenth
#     elif connect == max_connect and ans > line_lenth:
#         ans = line_lenth
#
# def processor_line_dir(n):
#     global processor_cnt
#     if n == processor_cnt:
#         cal_line_lenth()
#         return
#     for i in range(4):
#         processor[n][2] = i
#         processor_line_dir(n + 1)
#
# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     board = [list(map(int, input().split())) for _ in range(N)]
#     processor_cnt = 0
#     ans = 1 << 30
#     max_connect = 0
#     processor = []
#     for i in range(1, N - 1):
#         for j in range(1, N - 1):
#             if board[i][j] == 1:
#                 processor_cnt += 1
#                 processor.append([i, j, 0])
#     processor_line_dir(0)
#     print('#{} {}'.format(test_case, ans))