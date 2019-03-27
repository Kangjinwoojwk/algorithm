def merge(start, end):
    global cnt
    if end - start == 1:
        return
    n = (start + end) // 2
    harf = n
    s , e = start, end
    merge(start, n)
    merge(n, end)
    pivot = start
    while start != harf and n != end:
        if li[start] <= li[n]:
            result[pivot] = li[start]
            start += 1
            pivot += 1
        else:
            result[pivot] = li[n]
            n += 1
            pivot += 1
    if start == harf:
        for i in range(n, end):
            result[pivot] = li[i]
            pivot += 1
    else:
        for i in range(start, harf):
            result[pivot] = li[i]
            pivot += 1
        cnt += 1
    for i in range(s, e):
        li[i] = result[i]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cnt = 0
    li = list(map(int, input().split()))
    result = [0] * N
    merge(0, N)
    print('#{} {} {}'.format(tc, result[N//2], cnt))