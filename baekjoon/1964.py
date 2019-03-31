N = int(input())
ans = 1
cnt = 0
i = 4
while cnt < N:
    cnt += 1
    ans += i
    i += 3
print(ans % 45678)
