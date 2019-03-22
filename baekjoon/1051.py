N, M = map(int,input().split())
data = [list(map(int, list(input()))) for _ in range(N)]
ans = 1
limit = min(N, M)
for i in range(limit):
    for j in range(N - i):
        for k in range(M - i):
            if data[j][k] == data[j + i][k] == data[j][k + i] == data[j + i][k + i]:
                ans = (i + 1) ** 2
print(ans)