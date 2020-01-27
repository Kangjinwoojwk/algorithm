for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    n = set(input().split())
    m = set(input().split())
    answer = 0
    for i in n:
        if i in m:
            answer += 1
    print('#{} {}'.format(tc, answer))

'''
for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    n = list(input().split())
    m = list(input().split())
    answer = 0
    n.sort()
    m.sort()
    ni, mi = 0, 0
    while ni < N and mi < M:
        if n[ni] == m[mi]:
            answer += 1
            ni += 1
            mi += 1
            continue
        elif n[ni] < m[mi]:
            ni += 1
            continue
        elif n[ni] > m[mi]:
            mi += 1
            continue
    print('#{} {}'.format(tc, answer))

'''