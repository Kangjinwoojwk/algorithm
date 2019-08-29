for tc in range(1, int(input()) + 1):
    N = int(input())
    data = input().split()
    L = data[: (N + 1) >> 1]
    R = data[(N + 1) >> 1:]
    ans = list()
    for i in range(N >> 1):
        ans.append(L.pop(0))
        ans.append(R.pop(0))
    if L:
        ans.append(L.pop())
    print('#{}'.format(tc), end=' ')
    print(' '.join(ans))
