a, b = map(int, input().split())
if a > b:
    a, b = b, a
print(((b - a + 1) * (b + a)) // 2)