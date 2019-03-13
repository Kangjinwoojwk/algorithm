T = int(input())
for tc in range(1, T + 1):
    ans = 0
    A, B, C = map(int, input().split())
    if A <= B:
        ans += C // A
    else:
        ans += C // B
    print('#{} {}'.format(tc, ans))