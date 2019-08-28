back = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}
N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(6):
    n = 0
    for j in range(N):
        data[j][i] -= 100
        data[j][back[i]] -= 100
        n += max(data[j])
        data[j][i] += 100
        data[j][back[i]] += 100
        if j == N - 1:
            continue
        i = data[j + 1].index(data[j][back[i]])
    if n > ans:
        ans = n
print(ans)