N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N):
    data[i].sort()
for i in range(N):
    if data[i][0] == data[i][1] == data[i][2]:
        if ans < 10000 + 1000 * data[i][1]:
            ans = 10000 + 1000 * data[i][1]
    elif data[i][0] == data[i][1]:
        if ans < 1000 + 100 * data[i][1]:
            ans = 1000 + 100 * data[i][1]
    elif data[i][1] == data[i][2]:
        if ans < 1000 + 100 * data[i][1]:
            ans = 1000 + 100 * data[i][1]
    else:
        if ans < 100 * data[i][2]:
            ans = 100 * data[i][2]
print(ans)