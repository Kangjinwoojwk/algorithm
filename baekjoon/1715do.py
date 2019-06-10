n = int(input())
data = [int(input()) for _ in range(n)]
ans = 0
if n < 2:
    print(ans)
    exit()
else:
    data.sort()
    while len(data) >= 2:
        temp = data.pop(0) + data.pop(0)
        ans += temp
        for i in range(len(data)):
            if data[i] > temp:
                data.insert(i, temp)
                break
    print(ans)