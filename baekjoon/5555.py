search = input()
N = int(input())
ans = 0
for _ in range(N):
    a = input()
    a = a+a
    if search in a:
        ans += 1
print(ans)