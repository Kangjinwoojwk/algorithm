for _ in range(int(input())):
    n = int(input())
    result = list()
    i = 0
    while n:
        if n % 2:
            result.append(i)
        i += 1
        n //= 2
    print(' '.join(map(str, result)))