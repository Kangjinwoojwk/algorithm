def merge(li):
    global cnt
    n = len(li)
    if n == 1:
        return li
    L = merge(li[:n//2])
    R = merge(li[n//2:])
    result = []
    if L[-1] > R[-1]:
        cnt += 1
    while L and R:
        if L[0] < R[0]:
            result.append(L.pop(0))
        else:
            result.append(R.pop(0))
    if L:
        result.extend(L)
    else:
        result.extend(R)
    return result

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cnt = 0
    li = list(map(int, input().split()))
    li = merge(li)
    print('#{} {} {}'.format(tc, li[N//2], cnt))