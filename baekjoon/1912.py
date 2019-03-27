n = int(input())
li = list(map(int, input().split()))
ans = -1000
value = 0
for i in range(n):
    value += li[i]
    if value > ans:
        ans = value
    if value < 0:
        value = 0
print(ans)