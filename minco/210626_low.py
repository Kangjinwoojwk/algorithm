N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
rank = [N, N, 2 * N]
for i in data:
    if i[0] + i[1] < rank[2]:
        rank = [i[0], i[1], i[0] + i[1]]
    elif i[0] + i[1] == rank[2] and abs(i[0] - i[1]) < abs(rank[0] - rank[1]):
        rank = [i[0], i[1], i[0] + i[1]]
for i in range(N):
    if data[i][0] > rank[0] and data[i][1] > rank[1]:
        N -= 1
print(N)