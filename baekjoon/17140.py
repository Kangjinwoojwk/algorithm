def R(state):
    global data
    if state == 'C':
        data = [[data[j][i] for j in range(len(data))]for i in range(len(data[0]))]
    new_data = list()
    max_len = 0
    for i in data:
        temp = dict()
        for j in i:
            if j not in temp:
                temp[j] = 1
            else:
                temp[j] += 1
        temp = [(value, key) for key, value in temp.items() if key != 0]
        temp.sort()
        it = list()
        for p in temp:
            it.append(p[1])
            it.append(p[0])
        new_data.append(it[:100])
        n = len(it)
        if n > max_len:
            max_len = n
    for i in range(len(new_data)):
        for j in range(len(new_data[i]), max_len):
            new_data[i].append(0)
    data = new_data
    if state == 'C':
        data = [[data[j][i] for j in range(len(data))] for i in range(len(data[0]))]


r, c, k = map(int, input().split())
ans = 0
r -= 1
c -= 1
data = [list(map(int, input().split())) for _ in range(3)]
while (len(data) <= r or len(data[0]) <= c) or data[r][c] != k:
    if ans > 100:
        ans = -1
        break
    ans += 1
    if len(data) >= len(data[0]):
        R('R')
    else:
        R('C')
print(ans)