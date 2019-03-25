N = int(input())
data = [0] * 1001
for _ in range(N):
    a, b = map(int, input().split())
    data[a] = b
dp = [[0] * 1001 for _ in range(2)]
dp[0][0] = data[0]
dp[1][1000] = data[1000]
for i in range(1, 1001):
    dp[0][i] = max(dp[0][i - 1], data[i])
    dp[1][1000 - i] = max(dp[1][1000 - i + 1], data[1000 - i])
dpvalue = [min(dp[0][i], dp[1][i]) for i in range(1001)]
print(sum(dpvalue))