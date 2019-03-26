dp = [99999999] * 1000001
dp[1] = 0
for i in range(1, 1000000):
    if 3 * i <= 1000000:
        if dp[3 * i] > dp[i] + 1:
            dp[3 * i] = dp[i] + 1
    if 2 * i <= 1000000:
        if dp[2 * i] > dp[i] + 1:
            dp[2 * i] = dp[i] + 1
    if i + 1 <= 1000000:
        if dp[i + 1] > dp[i] + 1:
            dp[i + 1] = dp[i] + 1
print(dp[int(input())])
