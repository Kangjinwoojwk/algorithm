T = int(input())
wall = [[0]*100 for _ in range(100)]
for _ in range(T):
    sero, garo = map(int, input().split())
    for i in range(garo, garo + 10):
        for j in range(sero, sero + 10):
            wall[i][j] = 1
ans = 0
for i in range(100):
    for j in range(100):
        ans += wall[i][j]
print(ans)