N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
data.sort()
for i in data:
    print(i[0], i[1])