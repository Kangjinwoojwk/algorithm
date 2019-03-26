N = int(input())
li = []
end = 0
for _ in range(N):
    a, b = map(int, input().split())
    li.append((a, b))
    if b > end:
        end = b
li.sort()
data = [[] for i in range(end + 1)]
for i in li:
    data[i[0]].append(i[1])
dp = [0 for i in range(end + 1)]
for i in range(end + 1):
    if dp[i] < dp[i - 1]:
        dp[i] = dp[i - 1]
    for j in data[i]:
        if dp[j] < dp[i] + 1:
            dp[j] = dp[i] + 1
print(dp[end])