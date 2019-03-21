T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    time = [[] for _ in range(25)]
    dp = [0]*25
    for _ in range(N):
        s, e = map(int, input().split())
        time[s].append(e)
    for i in range(25):
        if dp[i - 1] > dp[i]:
            dp[i] = dp[i - 1]
        for j in time[i]:
            if dp[i] + 1 > dp[j]:
                dp[j] = dp[i] + 1
    print('#{} {}'.format(tc, dp[-1]))