N = int(input())
data = list(map(int, input().split()))
score = 1
ans = 0
for i in range(N):
    if data[i]:
        ans += score
        score += 1
    else:
        score = 1
print(ans)