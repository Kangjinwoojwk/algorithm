prime = [True] * 1001
prime[0] = prime[1] = False
i = 2
while i <= 1000:
    j = 2
    while i * j <= 1000:
        prime[i * j] = False
        j += 1
    i += 1
N = int(input())
li = list(map(int, input().split()))
ans = 0
for i in li:
    if prime[i]:
        ans += 1
print(ans)