def sol(x, y):
    global ans
    cnt1 = 0
    cnt2 = 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 and data[x + i][y + j] == 'W':
                cnt1 += 1
            if (i + j) % 2 and data[x + i][y + j] == 'B':
                cnt2 += 1
            if (i + j) % 2 == 0 and data[x + i][y + j] == 'B':
                cnt1 += 1
            if (i + j) % 2 == 0 and data[x + i][y + j] == 'W':
                cnt2 += 1
    if cnt1 < ans:
        ans = cnt1
    if cnt2 < ans:
        ans = cnt2
N, M = map(int, input().split())
ans = 64
data = [input() for _ in range(N)]
for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        sol(i, j)
print(ans)