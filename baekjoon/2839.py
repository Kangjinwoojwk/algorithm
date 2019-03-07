N = int(input())
ans = 0
while N % 10 != 0 and N % 10 != 5:
    N -= 3
    ans += 1
    if N < 0:
        ans = -1
        break
else:
    ans += N // 5
print(ans)