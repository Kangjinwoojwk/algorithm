N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
winner = 0
max_value = 0
for i in range(N):
    for j in range(5):
        for k in range(j + 1, 5):
            for l in range(k + 1, 5):
                value = (data[i][j] + data[i][k] + data[i][l]) % 10
                if max_value <= value:
                    max_value = value
                    winner = i + 1
print(winner)
