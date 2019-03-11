N = int(input())
li = list(map(int, input().split()))
up = 1
down = 1
max_lenth = 1
for i in range(1, N):
    if li[i - 1] <= li[i]:
        up += 1
    else:
        up = 1
    if li[i - 1] >= li[i]:
        down += 1
    else:
        down = 1
    if up > max_lenth:
        max_lenth = up
    if down > max_lenth:
        max_lenth = down
print(max_lenth)