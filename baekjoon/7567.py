data = input()
ans = 0
pre = ''
for i in data:
    if pre != i:
        ans += 5
    ans += 5
    pre = i
print(ans)