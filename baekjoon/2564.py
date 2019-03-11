garo, sero = map(int, input().split())
N = int(input())
direction = []
distance = []
for _ in range(N):
    a, b = map(int, input().split())
    direction.append(a)
    distance.append(b)
a, b = map(int, input().split())
sum_v = 0
for i in range(N):
    if a == direction[i]:
        sum_v += abs(b - distance[i])
    elif a == 1:
        if direction[i] == 2:
            sum_v += sero + min(2 * garo - distance[i] - b, distance[i] + b)
        elif direction[i] == 3:
            sum_v += distance[i] + b
        else:
            sum_v += distance[i] + garo - b
    elif a == 2:
        if direction[i] == 1:
            sum_v += sero + min(2 * garo - distance[i] - b, distance[i] + b)
        elif direction[i] == 3:
            sum_v += b + sero - distance[i]
        else:
            sum_v += sero + garo - distance[i] - b
    elif a == 3:
        if direction[i] == 1:
            sum_v += distance[i] + b
        elif direction[i] == 2:
            sum_v += sero - b + distance[i]
        else:
            sum_v = garo + min(2 * sero - distance[i] - b, distance[i] + b)
    elif a == 4:
        if direction[i] == 1:
            sum_v += b + garo - distance[i]
        elif direction[i] == 2:
            sum_v += garo + sero - distance[i] - b
        else:
            sum_v += garo + min(2 * sero - distance[i] - b, distance[i] + b)
print(sum_v)