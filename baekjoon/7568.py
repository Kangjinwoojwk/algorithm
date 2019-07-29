N = int(input())
data = list()
ans = [1]*N
for _ in range(N):
    a, b = map(int, input().split())
    data.append((a, b))
for i in range(N):
    for j in range(N):
        if i != j:
            if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
                ans[i] += 1
print(' '.join(map(str, ans)))