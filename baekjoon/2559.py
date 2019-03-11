N, K = map(int, input().split())
tempature = list(map(int, input().split()))
sum_temp = max_temp = sum(tempature[:K])
for i in range(K, N):
    sum_temp += tempature[i]
    sum_temp -= tempature[i - K]
    if sum_temp > max_temp:
        max_temp = sum_temp
print(max_temp)