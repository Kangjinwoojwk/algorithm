import sys
N, Q = map(int, sys.stdin.readline().split())
data = list(map(int, input().split()))
data.sort()
for i in range(1, N):
    data[i] += data[i - 1]
for _ in range(Q):
    a, b = map(int, sys.stdin.readline().split())
    if a == 1:
        print(data[b - 1])
    else:
        print(data[b - 1] - data[a - 2])