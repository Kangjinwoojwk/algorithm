for tc in range(1, int(input()) + 1):
    N = int(input())
    K = int(input())
    li = list(map(int, input().split()))
    li.sort()
    distance = list()
    for i in range(1, N):
        distance.append(li[i] - li[i - 1])
    distance.sort()
    ans = li[-1] - li[0]
    for i in range(K - 1):
        if distance:
            ans -= distance[-1]
            del distance[-1]
    print('#{} {}'.format(tc, ans))