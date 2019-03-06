N, K = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N - 1, 0, -1):
        if li[j][1] > li[j - 1][1]:
            li[j], li[j - 1] = li[j - 1], li[j]
for i in range(N):
    for j in range(N - 1, 0, -1):
        if li[j][1] == li[j - 1][1] and li[j][2] > li[j - 1][2]:
            li[j], li[j - 1] = li[j - 1], li[j]
for i in range(N):
    for j in range(N - 1, 0, -1):
        if li[j][1] == li[j - 1][1] and li[j][2] == li[j - 1][2] and li[j][3] > li[j - 1][3]:
            li[j], li[j - 1] = li[j - 1], li[j]
for i in range(0, N):
    if i == 0:
        li[i].append(i + 1)
        continue
    if li[i][1] == li[i - 1][1] and li[i][2] == li[i - 1][2] and li[i][3] == li[i - 1][3]:
        li[i].append(li[i - 1][4])
        continue
    li[i].append(i + 1)
for i in range(0, N):
    if li[i][0] == K:
        print(li[i][4])
        break