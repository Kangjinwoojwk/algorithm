N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0, 0, 0] for _ in range(N)] for __ in range(N)]
dp[0][1][1] = 1
for i in range(2, 2 * N):
    for j in range(i):
        if 0 <= j < N and 0 <= i - j < N and data[j][i - j] == 0:
            if 0 <= i - j - 1 < N:
                dp[j][i - j][1] = dp[j][i - j - 1][1] + dp[j][i - j - 1][0]
            if 0 <= j - 1 < N:
                dp[j][i - j][2] = dp[j - 1][i - j][2] + dp[j - 1][i - j][0]
            if 0 <= j - 1 < N and 0 <= i - j - 1 < N and data[j - 1][i - j] == data[j][i - j - 1] == 0:
                dp[j][i - j][0] = dp[j - 1][i - j - 1][0] + dp[j - 1][i - j - 1][1] + dp[j - 1][i - j - 1][2]
print(sum(dp[N-1][N-1]))

# 시간 터짐
# def sol(tx, ty, hx, hy):
#     global N, ans
#     if hx == hy == N - 1:
#         ans += 1
#         return
#     if hx == tx:
#         if hy + 1 < N and data[hx][hy + 1] == 0:
#             sol(hx, hy, hx, hy + 1)
#         if hy + 1 < N and hx + 1 < N and data[hx][hy + 1] == data[hx + 1][hy + 1] == data[hx + 1][hy] == 0:
#             sol(hx, hy, hx + 1, hy + 1)
#     elif hy == ty:
#         if hx + 1 < N and data[hx + 1][hy] == 0:
#             sol(hx, hy, hx + 1, hy)
#         if hy + 1 < N and hx + 1 < N and data[hx][hy + 1] == data[hx + 1][hy + 1] == data[hx + 1][hy] == 0:
#             sol(hx, hy, hx + 1, hy + 1)
#     else:
#         if hy + 1 < N and data[hx][hy + 1] == 0:
#             sol(hx, hy, hx, hy + 1)
#         if hx + 1 < N and data[hx + 1][hy] == 0:
#             sol(hx, hy, hx + 1, hy)
#         if hy + 1 < N and hx + 1 < N and data[hx][hy + 1] == data[hx + 1][hy + 1] == data[hx + 1][hy] == 0:
#             sol(hx, hy, hx + 1, hy + 1)
#
# N = int(input())
# data = [list(map(int, input().split())) for _ in range(N)]
# ans = 0
# sol(0, 0, 0, 1)
# print(ans)