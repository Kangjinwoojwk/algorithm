for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    li = list(map(int, input().split()))
    resultvalue = [li[i + 1] - li[i] if li[i + 1] > li[i] else li[i] - li[i + 1]for i in range(N - 1)]
    resultdir = [li[i] < li[i + 1]for i in range(N - 1)]
    while K:
        check = resultvalue.index(max(resultvalue))
        resultvalue[check] -= 1



        K-=1