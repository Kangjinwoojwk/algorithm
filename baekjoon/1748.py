N = int(input())
ans = 0
i = 1
j = 1
while N // (10 * i):
    ans += 9 * i * j
    i *= 10
    j += 1
ans += j * (N - i + 1)
print(ans)
