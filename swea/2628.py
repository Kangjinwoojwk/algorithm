W, H = map(int, input().split())
N = int(input())
li = [[0], [0]]
for _ in range(N):
    a, b = map(int, input().split())
    if a == 0:
        li[0].append(b)
    else:
        li[1].append(b)
li[0].sort()
li[1].sort()
li[0].append(H)
li[1].append(W)
li_0 = len(li[0])
li_1 = len(li[1])
max_v= 0
for i in range(li_0 - 1):
    for j in range(li_1 - 1):
        m = (li[0][i + 1] - li[0][i]) * (li[1][j + 1] - li[1][j])
        if m > max_v:
            max_v = m
print(max_v)