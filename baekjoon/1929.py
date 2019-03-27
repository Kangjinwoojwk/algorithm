prime = [True] * 1000001
prime[0] = prime[1] = False
i = 2
while i <= 1000000:
    j = 2
    while i * j <= 1000000:
        prime[i * j] = False
        j += 1
    i += 1
M, N = map(int, input().split())
for i in range(M, N + 1):
    if prime[i]:
        print(i)