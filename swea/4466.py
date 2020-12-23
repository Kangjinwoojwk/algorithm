T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    data = list(map(int, input().split()))
    data.sort(reverse=True)
    ans = 0
    for i in range(K):
        ans += data[i]
    print('#{} {}'.format(tc, ans))