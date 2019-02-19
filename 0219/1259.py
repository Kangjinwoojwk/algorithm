import sys
sys.stdin = open('1259.txt', 'r')
sys.stdout = open('1259_out.txt', 'w')
T = int(input())


def sol(data):
    n = len(data)
    if n == 1:
        return
    for i in range(1, n):
        if data[i][0] == data[0][-1]:
            data[0] = data[0] + data[i]
            data[:] = data[:i]+data[i + 1:]
            sol(data)
            break
        if data[i][-1] == data[0][0]:
            data[i] = data[i] + data[0]
            data[:] = data[1:]
            sol(data)
            break


for test_case in range(1, T + 1):
    n = int(input())
    get_data = list(map(int, input().split()))
    get_data = [get_data[2 * i:2 * i + 2]for i in range(n)]
    sol(get_data)
    print(f'#{test_case} ' + ' '.join([str(i) for i in get_data[0]]))
# T = int(input())
# for test_case in range(1, T + 1):
#     n = int(input())
#     get_data = list(map(int, input().split()))
#     ans = get_data[0:2]
#     get_data = get_data[2:]
#     n -= 1
#     k = 0
#     while n > 0:
#         if k == 0:
#             for i in range(n):
#                 if get_data[2 * i + k] == ans[-1]:
#                     ans = ans + get_data[2 * i + k:2 * i + k + 2]
#                     get_data = get_data[:2 * i + k] + get_data[2 * i + k + 2:]
#                     n -= 1
#                     break
#             else:
#                 k = 1
#         elif k == 1:
#             for i in range(n):
#                 if get_data[2 * i + k] == ans[0]:
#                     ans = get_data[2 * i + k - 1:2 * i + k + 1] + ans
#                     get_data = get_data[:2 * i + k - 1] + get_data[2 * i + k + 1:]
#                     n -= 1
#                     break
#             else:
#                 n = 0
#     print(f'#{test_case} ' + ' '.join([str(i) for i in ans]))
