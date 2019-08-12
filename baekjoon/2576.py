minimum = 100
ans = 0
for i in range(7):
    a = int(input())
    if a % 2:
        ans += a
        if a < minimum:
            minimum = a
if ans:
    print(ans)
    print(minimum)
else:
    print(-1)