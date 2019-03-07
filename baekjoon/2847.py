N = int(input())
li = []
for _ in range(N):
    li.append(int(input()))
ans = 0
for i in range(N - 1, 0, -1):
    if li[i - 1] >= li[i]:
        ans += li[i - 1] - li[i] + 1
        li[i - 1] = li[i] - 1
print(ans)