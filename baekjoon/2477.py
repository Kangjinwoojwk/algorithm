K = int(input())
direction = []
length = []
for _ in range(6):
    a, b = map(int, input().split())
    direction.append(a)
    length.append(b)
direction *= 2
# lenth도 같이 늘려주지 않으면 후예 계산할때 범위 넘어가서 런타임 에러
length *= 2
big = 0
small = 0
for i in range(12):
    if direction[i] == direction[i + 2] and direction[i + 1] == direction[i + 3]:
        small = length[i + 1] * length[i + 2]
        big = length[i - 1] * length[i - 2]
        break
print((big-small) * K)