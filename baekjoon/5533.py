N = int(input())
user = [[] for _ in range(N)]
score = [0] * N
for _ in range(N):
    user[_] = list(map(int, input().split()))
for i in range(3):
    di = {}
    for j in range(N):
        if user[j][i] in di:
            di[user[j][i]] += 1
        else:
            di[user[j][i]] = 1
    for j in range(N):
        if di[user[j][i]] == 1:
            score[j] += user[j][i]
print('\n'.join(map(str, score)))