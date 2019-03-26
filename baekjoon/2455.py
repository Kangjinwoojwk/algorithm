ans = 0
value = 0
for _ in range(4):
    a, b = map(int, input().split())
    value += b - a
    if value > ans:
        ans = value
print(ans)