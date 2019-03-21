T = int(input())
for tc in range(1, T + 1):
    a, get = input().split()
    get = [int(i) if 47 < ord(i) < 58 else ord(i) - 55 for i in get]
    result = [''] * len(get)
    for idx, value in enumerate(get):
        for j in range(4):
            result[idx] = str(value % 2) + result[idx]
            value //= 2
    print('#{} {}'.format(tc, ''.join(result)))