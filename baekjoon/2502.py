D, K = map(int, input().split())
pibo = [1, 1, 2, 3, 5]
for i in range(5, 31):
    pibo.append(pibo[i - 1] + pibo[i - 2])
D -= 3
answer = list()
for i in range(1, 1000000):
    for j in range(i, 1000000):
        if (i * pibo[D] + j * pibo[D + 1]) == K:
            answer = [i, j]
            break
    if answer:
        break
print('\n'.join(map(str, answer)))