N = int(input())
a = 1
for i in range(1, N + 1):
    a *= i
ans = 0
while a % 10 == 0:
    ans += 1
    a //= 10
print(ans)