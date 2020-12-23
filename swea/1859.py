T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    ans = 0
    li = list(map(int, input().split()))
    for i in range(N - 1, -1, -1):
        if li[N - 1] > li[i]:
            ans += li[N - 1] - li[i]
        elif li[N - 1] < li[i]:
            li[N - 1], li[i] = li[i], li[N - 1]
    print('#{} {}'.format(tc, ans))