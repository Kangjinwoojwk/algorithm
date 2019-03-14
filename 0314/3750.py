T = int(input())
dop = [int(input()) for _ in range(T)]
for i in range(T):
    while dop[i] >= 10:
        dop[i] = dop[i] // 10 + dop[i] % 10
for i in range(T):
    dop[i] = '#'+str(i + 1)+' '+ str(dop[i])
print('\n'.join(dop))