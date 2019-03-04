import sys
sys.stdin = open('5176.txt', 'r')
sys.stdout = open('5176_out.txt', 'w')
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    i = 1
    full = 1
    while full < N:
        i *= 2
        full += i
    full_save = full
    full -= i
    i //= 2
    left = (full//2)
    if N - full >= i:
        left += i
    else:
        left += (N - full)
    root = left + 1 # root 부터 구한다.
    binary_list = [root for _ in range(N + 1)]
    
    print('#{} {} {}'.format(test_case, root, binary_list[N // 2]))








# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     i = 1
#     full = 1
#     while full < N:
#         i *= 2
#         full += i
#     full -= i
#     i //= 2
#     left = (full//2)
#     if N - full >= i:
#         left += i
#     else:
#         left += (N - full)
#         i //= 2
#     root = left + 1
#     binary_list = [root for _ in range(N)]
#     chk = 2
#     chk_chk = 0
#     for j in range(1, N):
#         if j % 2:
#             binary_list[j] = binary_list[(j - 1) // 2] - i
#             chk_chk += 1
#
#         else :
#             binary_list[j] = binary_list[(j - 1) // 2] + i
#             chk_chk += 1
#         if chk == chk_chk:
#             chk *= 2
#             chk_chk = 0
#             i //= 2
#     print('#{} {} {}'.format(test_case, root, binary_list[N // 2 - 1]))

