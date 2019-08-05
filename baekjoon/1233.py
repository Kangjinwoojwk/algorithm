S1, S2, S3 = map(int, input().split())
data = [0] * 81
max_data = 0
for i1 in range(1, S1 + 1):
    for i2 in range(1, S2 + 1):
        for i3 in range(1, S3 + 1):
            data[i1 + i2 + i3] += 1
            if data[i1 + i2 + i3] > max_data:
                max_data = data[i1 + i2 + i3]
for i in range(1, 81):
    if data[i] == max_data:
        print(i)
        exit()
# 기대값으로 풀면 안되나 보다
# S1, S2, S3 = map(int, input().split())
# ans = ((S1+1)/2) + ((S2 + 1)/2) + ((S3 + 1)/2)
# print(int(ans))