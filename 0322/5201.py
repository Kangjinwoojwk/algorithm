T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    container.sort()
    truck.sort()
    ans = 0
    i = len(container) - 1
    j = len(truck) - 1
    while i >= 0 and j >= 0:
        if truck[j] >= container[i]:
            ans += container[i]
            i -= 1
            j -= 1
        else:
            i -= 1
    print('#{} {}'.format(tc, ans))
