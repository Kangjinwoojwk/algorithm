while True:
    n = int(input())
    if n == -1:
        break
    ans = list()
    for i in range(1, (n // 2) + 1):
        if n % i:
            continue
        ans.append(i)
    if sum(ans) == n:
        print(n, '=', end=' ')
        print(' + '.join(map(str, ans)))
    else:
        print('{} is NOT perfect.'.format(n))