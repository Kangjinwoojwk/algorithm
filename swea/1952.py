for tc in range(1, int(input()) + 1):
    day, month, three_month, year = map(int, input().split())
    dp = list(map(int, input().split()))
    dp.insert(0, 0)
    dp.append(0)
    for i in range(1, 13):
        dp[i] = dp[i] * day
    for i in range(1, 13):
        if dp[i] > month:
            dp[i] = month
    for i in range(2, 13):
        dp[i] = min(dp[i - 1] + dp[i], dp[i - 3] + three_month)
    print('#{} {}'.format(tc, min(dp[12], year)))