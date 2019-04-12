data = [[0] * 101 for _ in range(101)]
N = int(input())
for i in range(1, N + 1):
    x, y, weight, height = map(int, input().split())
    for j in range(x, x + weight):
        for k in range(y, y + height):
            data[j][k] = i
cnt = [0] * (N + 1)
for i in range(101):
    for j in range(101):
        cnt[data[i][j]] += 1
for i in range(1, N + 1):
    print(cnt[i])
