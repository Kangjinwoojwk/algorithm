N = int(input())
for i in [sum(map(int, input().split(','))) for _ in range(N)]:
    print(i)