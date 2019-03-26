N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1
for i in range(2 * (N - 1)):
    for j in range(i + 1):
        if 0 <= i - j < N and 0 <= j < N:
            if 0 <= i - j + data[i - j][j] < N:
                dp[i - j + data[i - j][j]][j] += dp[i - j][j]
            if 0 <= j + data[i - j][j] < N:
                dp[i - j][j + data[i - j][j]] += dp[i - j][j]
print(dp[N - 1][N - 1])
