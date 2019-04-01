N, M, K = map(int, input().split())
x, y = (K - 1) // M + 1, ((K - 1) % M) + 1
if K == 0:
    x = y = 1
pre = 1
for i in range(1, x + y - 1):
    pre *= i
for i in range(1, x):
    pre //= i
for i in range(1, y):
    pre //= i
post = 1
for i in range(1, N + M - x - y + 1):
    post *= i
for i in range(1, N - x + 1):
    post //= i
for i in range(1, M - y + 1):
    post //= i
print(pre * post)