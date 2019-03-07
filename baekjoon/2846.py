N = int(input())
way = list(map(int, input().split()))
max_up = 0
up_length = 0
for i in range(1, N):
    if way[i] > way[i - 1]:
        up_length += way[i] - way[i - 1]
        if up_length > max_up:
            max_up = up_length
    else:
        up_length = 0
print(max_up)