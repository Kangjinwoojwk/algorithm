N = int(input())
li = list(map(int, input().split()))
li.sort()
ans = 0
for i in range(N):
    ans += li[i] * (N - i)
print(ans)