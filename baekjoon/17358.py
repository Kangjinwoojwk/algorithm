N = int(input())
ans = 1
while N:
    ans *= (N - 1)
    N -= 2
print(ans % 1000000007)