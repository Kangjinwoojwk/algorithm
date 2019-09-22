n, m = map(int, input().split())
x, y = map(int, input().split())
if x > n or y > m:
    print('fail')
else:
    ans = 1
    for i in range(1, x + y + 1):
        ans *= i
    for i in range(1, x + 1):
        ans //= i
    for i in range(1, y + 1):
        ans //= i
    print(x + y)
    print(ans)