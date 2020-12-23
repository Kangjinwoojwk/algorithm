won = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
T = int(input())
for tc in range(1, T + 1):
    geo = [0] * 8
    N = int(input())
    for i in range(8):
        geo[i] = N // won[i]
        N %= won[i]
    print('#{}'.format(tc))
    print(' '.join(map(str,geo)))