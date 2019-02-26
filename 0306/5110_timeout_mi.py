import sys
sys.stdin = open('5110.txt', 'r')
sys.stdout = open('5110_out.txt', 'w')
T = int(input())
for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    data = [list(map(int, input().split())) for _ in range(M)]
    ptr = [[0, 0]]
    i = 0
    j = 1
    for _ in range(M - 1):
        while i < (_ + 1) * N:
            if data[0][i] > data[1][0]:
                data[0] = data[0][:i] + data[1] + data[0][i:]
                data = data[:1] + data[2:]
                ptr = ptr[:j] + [[data[0][i], i]] + ptr[j:]
                for k in range(j + 1, len(ptr)):
                    ptr[k][1] += N
                if _ != M - 2:
                    j = 0
                    while j < len(ptr):
                        if ptr[j][0] > data[1][0]:
                            i = ptr[j - 1][1]
                            break
                        j += 1
                    else:
                        i = ptr[-1][1]
                break
            i += 1
        else:
            data[0] = data[0][:] + data[1]
            data = data[:1] + data[2:]
            ptr.append([data[0][i], i])
            if _ != M - 2:
                j = 0
                while j < len(ptr):
                    if ptr[j][0] > data[1][0]:
                        i = ptr[j - 1][1]
                        break
                    j += 1
                else:
                    i = ptr[-1][1]
    data = data[0]
    print('#{}'.format(test_case), end='')
    if len(data) >= 10:
        for i in range(1, 11):
            print(' {}'.format(data[-i]), end='')
    else:
        for i in range(1, len(data) + 1):
            print(' {}'.format(data[-i]), end='')
    print()



# 붙일 때마다 하나하나 포인트 잡아서 그 포인트로 순간 이동해서 하게 했다.
# 또 9/10 시간 초과다....
# 하아...이렇게 했는데도 시간 초과야...
# T = int(input())
# for test_case in range(1, T + 1):
#     N, M = list(map(int, input().split()))
#     data = [list(map(int, input().split())) for _ in range(M)]
#     ptr = [[0, 0]]
#     i = 0
#     j = 1
#     for _ in range(M - 1):
#         while i < (_ + 1) * N:
#             if data[0][i] > data[1][0]:
#                 data[0] = data[0][:i] + data[1] + data[0][i:]
#                 data = data[:1] + data[2:]
#                 ptr = ptr[:j] + [[data[0][i], i]] + ptr[j:]
#                 for k in range(j + 1, len(ptr)):
#                     ptr[k][1] += N
#                 if _ != M - 2:
#                     j = 0
#                     while j < len(ptr):
#                         if ptr[j][0] > data[1][0]:
#                             i = ptr[j - 1][1]
#                             break
#                         j += 1
#                     else:
#                         i = ptr[-1][1]
#                 break
#             i += 1
#         else:
#             data[0] = data[0][:] + data[1]
#             data = data[:1] + data[2:]
#             ptr.append([data[0][i], i])
#             if _ != M - 2:
#                 j = 0
#                 while j < len(ptr):
#                     if ptr[j][0] > data[1][0]:
#                         i = ptr[j - 1][1]
#                         break
#                     j += 1
#                 else:
#                     i = ptr[-1][1]
#     data = data[0]
#     print('#{}'.format(test_case), end='')
#     if len(data) >= 10:
#         for i in range(1, 11):
#             print(' {}'.format(data[-i]), end='')
#     else:
#         for i in range(1, len(data) + 1):
#             print(' {}'.format(data[-i]), end='')
#     print()


# 명세대로 작성하되 이전꺼에서 그대로 작성하니 시간이 터져 버렸으므로
# 이번에는 시간을 줄이기 위해 앞서 합칠때 이미 본 것은 이전 데이터의 맨 앞보다 작다는
# 사실을 이용해서 연산을 줄였다.
# 그러나 또 제한시간 초과
# T = int(input())
# for test_case in range(1, T + 1):
#     N, M = list(map(int, input().split()))
#     data = [list(map(int, input().split())) for _ in range(M)]
#     i = 0
#     for _ in range(M - 1):
#         while i < (_ + 1) * N:
#             if data[0][i] > data[1][0]:
#                 data[0] = data[0][:i] + data[1] + data[0][i:]
#                 data = data[:1] + data[2:]
#                 if _ != M - 2 and data[0][i] > data[1][0]:
#                     i = 0
#                 break
#             i += 1
#         else:
#             data[0] = data[0][:] + data[1]
#             data = data[:1] + data[2:]
#             if _ != M - 2 and data[0][i] > data[1][0]:
#                 i = 0
#     data = data[0]
#     print('#{}'.format(test_case), end='')
#     if len(data) >= 10:
#         for i in range(1, 11):
#             print(' {}'.format(data[-i]), end='')
#     else:
#         for i in range(1, len(data) + 1):
#             print(' {}'.format(data[-i]), end='')
#     print()


# 명세 그대로 작성 일일이 보면서 합쳐준다- 시간 초과
# T = int(input())
# for test_case in range(1, T + 1):
#     N, M = list(map(int, input().split()))
#     data = [list(map(int, input().split())) for _ in range(M)]
#     for _ in range(M - 1):
#         for i in range(N * (_ + 1)):
#             if data[0][i] > data[1][0]:
#                 data[0] = data[0][:i] + data[1] + data[0][i:]
#                 data = data[:1] + data[2:]
#                 break;
#         else:
#             data[0] = data[0][:] + data[1]
#             data = data[:1] + data[2:]
#     data = data[0]
#     print('#{}'.format(test_case), end='')
#     if len(data)>=10:
#         for i in range(1, 11):
#             print(' {}'.format(data[-i]), end='')
#     else:
#         for i in range(1, len(data) + 1):
#             print(' {}'.format(data[-i]), end='')
#     print()
