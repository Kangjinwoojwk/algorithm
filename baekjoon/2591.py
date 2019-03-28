N = input()
dp = [0] * len(N)
if N[0] > '0':
    dp[0] = 1
else:
    dp[0] = 0
if len(N) > 1:
    if N[1] > '0':
        dp[1] += dp[0]
    if '0' < N[0] < '3':
        dp[1] += dp[0]
    elif N[0] == '3' and '0' <= N[1] <= '4':
        dp[1] += dp[0]
for i in range(2, len(N)):
    if N[i] > '0':
        dp[i] += dp[i - 1]
    if '0' < N[i - 1] < '3':
        dp[i] += dp[i - 2]
    elif N[i - 1] == '3' and '0' <= N[i] <= '4':
        dp[i] += dp[i - 2]
print(dp[-1])




# 답은 나오지만...시간 초과
# def sol(n):
#     global ans
#     if n == 0:
#         ans += 1
#         return
#     if n % 10:
#         sol(n // 10)
#     if 10 <= n % 100 <= 34:
#         sol(n // 100)
#     if n % 100 == 0:
#         ans = 0
#         return
#     if n % 10 == 0 and n % 100 > 35:
#         ans = 0
#         return
# N = int(input())
# ans = 0
# if N:
#     sol(N)
# print(ans)