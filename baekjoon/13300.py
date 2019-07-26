N, K = map(int, input().split())
data = [[0]*6 for _ in range(2)]
for _ in range(N):
    a, b = map(int, input().split())
    data[a][b-1] += 1
ans = 0
for i in range(2):
    for j in range(6):
        while data[i][j] > 0:
            ans += 1
            data[i][j] -= K
print(ans)