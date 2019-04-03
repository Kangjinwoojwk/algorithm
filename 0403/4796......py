for tc in range(1, int(input()) + 1):
    N = int(input())
    li = list(map(int, input().split()))
    ans = 0
    pre = 0
    post = 0
    i = 1
    while i < N:
        if li[i - 1] < li[i]:
            if post:
                ans += pre * post
                pre = 0
                post = 0
            pre += 1
        elif li[i - 1] > li[i]:
            post += 1
        i += 1
    if post:
        ans += pre * post
    print('#{} {}'.format(tc, ans))