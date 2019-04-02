N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
ans = 1
max_known = 0
for i in range(N):
    visit = [True] * N
    for j in range(5):
        for k in range(N):
            if i == k:
                continue
            if data[i][j] == data[k][j]:
                visit[k] = False
    a = visit.count(False)
    if a > max_known:
        max_known = a
        ans = i + 1
print(ans)