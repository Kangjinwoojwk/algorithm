import sys
sys.stdin = open('1210.txt', 'r')
sys.stdout = open('1210_out.txt', 'w')
for _ in range(10):
    test_case = int(input())
    ladder_map = [list(map(int, input().split())) for _ in range(100)]
    X = 0
    for i in range(100):
        if ladder_map[99][i] == 2:
            X = i
    i = 99
    while i > 0:
        if X - 1 >= 0 and ladder_map[i][X - 1] == 1:
            for j in range(1, 100):
                if X - j == -1 or ladder_map[i][X - j] == 0:
                    X -= j - 1
                    break
        elif X + 1 < 100 and ladder_map[i][X + 1] == 1:
            for j in range(1, 100):
                if X + j == 100 or ladder_map[i][X + j] == 0:
                    X += j - 1
                    break
        i -= 1
    print('#{} {}'.format(test_case, X))



# def sol(cnt, X, dir):
#     global ladder_map
#     if cnt == 0:
#         return X
#     if dir == 2:
#         if X + 1 < 100 and ladder_map[cnt][X + 1] == 1:
#             return sol(cnt, X + 1, 2)
#         else:
#             return sol(cnt - 1, X, 0)
#     elif dir == 1:
#         if X - 1 >= 0 and ladder_map[cnt][X - 1] == 1:
#             return sol(cnt, X - 1, 1)
#         else:
#             return sol(cnt - 1, X, 0)
#     else:
#         if X - 1 >= 0 and ladder_map[cnt][X - 1] == 1:
#             return sol(cnt, X - 1, 1)
#         elif X + 1 < 100 and ladder_map[cnt][X + 1] == 1:
#             return sol(cnt, X + 1, 2)
#         else:
#             return sol(cnt - 1, X, 0)
#
#
# for _ in range(10):
#     test_case = int(input())
#     ladder_map = [list(map(int, input().split())) for __ in range(100)]
#     X = 0
#     for i in range(100):
#         if ladder_map[99][i] == 2:
#             X = i
#     ans = sol(99, X, 0)
#     print('#{} {}'.format(test_case, ans))
