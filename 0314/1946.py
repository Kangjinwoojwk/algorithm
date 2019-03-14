T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    result = []
    long = 0
    for i in range(N):
        a, b = input().split()
        b = int(b)
        long += b
        for j in range(b):
            result.append(a)
    i = 0
    print('#{}'.format(tc))
    while i < long:
        print(''.join(result[i:i + 10]))
        i += 10