li = [[0] * 10 for _ in range(10)]
for i in range(10):
    li[i][i] = li[i][0] = 1
for i in range(2, 10):
    for j in range(1, i ):
        li[i][j] = li[i - 1][j - 1]+li[i - 1][j]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print('#{}'.format(tc))
    for i in range(N):
        for j in range(i + 1):
            print(li[i][j], end='')
            if j == i:
                pass
            else:
                print(' ', end='')
        print()