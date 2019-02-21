import sys
sys.stdin = open('1216.txt', 'r')
sys.stdout = open('1216_out.txt', 'w')

for test_case in range(10):
    test_num = int(input())
    arr = [input() for _ in range(100)]
    ans = 0
    for i in range(100):
        for j in range(100):
            x = 1
            y = 1
            while i - x >= 0 and i + x < 100:
                if arr[i - x][j] == arr[i + x][j]:
                    x += 1
                else:
                    break
            if 2 * (x - 1) + 1 > ans:
                ans = 2 * (x - 1) + 1
            while j - y >= 0 and j + y < 100:
                if arr[i][j - y] == arr[i][j + y]:
                    y += 1
                else:
                    break
            if 2 * (y - 1) + 1 > ans:
                ans = 2 * (y - 1) + 1
            x = 1
            y = 1
            while i - x >= 0 and i + x - 1 < 100:
                if arr[i - x][j] == arr[i + x - 1][j]:
                    x += 1
                else:
                    break
            if 2 * (x - 1) > ans:
                ans = 2 * (x - 1)
            while j - y >= 0 and j + y - 1 < 100:
                if arr[i][j - y] == arr[i][j + y - 1]:
                    y += 1
                else:
                    break
            if 2 * (y - 1) > ans:
                ans = 2 * (y - 1)
    print(f'#{test_num} {ans}')


























# def hoemun(a):
#     n = len(a) >> 1
#     for i in range(n):
#         if a[i] != a[-(i + 1)]:
#             return False
#     return True
#
#
# for test_case in range(10):
#     test_num = int(input())
#     arr = [input() for _ in range(100)]
#     ans = 0
#     i = 100
#     while i > ans:
#         for j in range(100):
#             for k in range(101 - i):
#                 if hoemun(arr[j][k:k + i]):
#                     ans = i
#                     break
#                 if hoemun(''.join([arr[l][j] for l in range(k, k + i)])):
#                     ans = i
#                     break
#             if ans == i:
#                 break
#         i -= 1
#     print(f'#{test_num} {ans}')
