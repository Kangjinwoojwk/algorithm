N = int(input())
li = list(map(int, input().split()))
Y = 0
M = 0
for i in range(N):
    if li[i] == 0:
        continue
    Y += 10 * ((li[i] + 30) // 30)
    M += 15 * ((li[i] + 60) // 60)
if Y == M:
    print('Y M {}'.format(Y))
elif Y < M:
    print('Y {}'.format(Y))
elif Y > M:
    print('M {}'.format(M))
