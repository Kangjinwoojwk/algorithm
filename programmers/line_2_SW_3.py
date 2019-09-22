N = int(input())
toilet = [0] * 151
for i in range(N):
    s, e = map(int, input().split())
    for j in range(s, e):
        toilet[j] += 1
print(max(toilet))