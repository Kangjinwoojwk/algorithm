memo = [0] * 100
memo[0] = 0
memo[1] = 1
for i in range(2, 41):
    memo[i] = memo[i - 1] + memo[i - 2]

print(memo[40])









# memo = [0] * 101
#
#
# def fibo(n):
#     if n < 2: return n
#     if memo[n] != 0:
#         return memo[n]
#     else:
#         memo[n] = fibo(n - 1) + fibo(n - 2)
#         return memo[n]
#
#
# print(fibo(40))