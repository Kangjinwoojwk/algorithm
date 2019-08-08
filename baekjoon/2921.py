ans = 0
for i in range(int(input()) + 1):
    for j in range(i, 2 * i + 1):
        ans += j
print(ans)