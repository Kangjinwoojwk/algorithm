data = [0] * 1001
data[0] = data[1] = 1
n = int(input())
for i in range(2, n + 1):
    data[i] = data[i - 2] * 2 + data[i - 1]
print(data[n]%10007)