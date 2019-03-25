n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
dp = [10000000] * (k + 1)
dp[0] = 0
for i in range(k):
    for j in coin:
        if i + j <= k:
            if dp[i + j] > dp[i] + 1:
                dp[i + j] = dp[i] + 1
if dp[k] == 10000000:
    print(-1)
else:
    print(dp[k])



# 시간 초과, dp를 써야 할거 같다.
# def sol(ptr, cnt, k):
#     global ans
#     if k == 0:
#         if ans > cnt:
#             ans = cnt
#         return
#     if cnt >= ans:
#         return
#     if ptr == len(coin):
#         return
#     for i in range(k // coin[ptr] + 1):
#         sol(ptr + 1, cnt + i, k - (coin[ptr] * i))
# n, k = map(int, input().split())
# coin = [int(input()) for _ in range(n)]
# ans = 2**30
# coin.sort(reverse=True)
# sol(0, 0, k)
# if ans == 2**30:
#     ans = -1
# print(ans)