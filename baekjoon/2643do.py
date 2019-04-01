N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
data.sort(key=lambda sqr: sqr[0] * sqr[1], reverse=True)
dp = [1] * N
for i in range(N):
    for j in range(i + 1, N):
        if min(data[i]) == min(data[j]) and max(data[i]) == max(data[j]):
            pass
        elif min(data[i]) >= min(data[j]) and max(data[i]) >= max(data[j]):
            if dp[j] < dp[i] + 1:
                dp[j] = dp[i] + 1
print(max(dp))