result = [1, 0]
N = int(input())
for _ in range(N):
    x, y = result
    result[0] = y
    result[1] = x + y
print(' '.join(map(str, result)))