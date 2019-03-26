X = int(input())
N = 64
ans = 0
while X:
    if X // N:
        X -= N
        ans += 1
    N //= 2
print(ans)