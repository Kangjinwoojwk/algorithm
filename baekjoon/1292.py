data = [0] + [i for i in range(1, 50) for j in range(i)]
a, b = map(int, input().split())
print(sum(data[a:b + 1]))