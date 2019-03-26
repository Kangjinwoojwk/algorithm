N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
for i in range(1, N):
    data[i][0] += min(data[i - 1][1], data[i - 1][2])
    data[i][1] += min(data[i - 1][0], data[i - 1][2])
    data[i][2] += min(data[i - 1][0], data[i - 1][1])
print(min(data[N - 1]))








# 시간 초과, dp를 써야 하나 보다
# import sys
# sys.setrecursionlimit(5000)
# def sol(house, RGB, price):
#     global N, ans
#     if house == N:
#         if price < ans:
#             ans = price
#         return
#     if price >= ans:
#         return
#     for i in range(3):
#         if RGB == i:
#             continue
#         sol(house + 1, i, price + data[house][i])
# N = int(input())
# data = [list(map(int, input().split())) for _ in range(N)]
# ans = 2**30
# sol(0, -1, 0)
# print(ans)