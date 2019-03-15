T = int(input())
for _ in range(T):
    N = input()
    score = 0
    sco = 1
    for i in N:
        if i == 'O':
            score += sco
            sco += 1
        else:
            sco = 1
    print(score)