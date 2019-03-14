T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    ans = -1
    while x < M * N or y < M * N:
        if x < y:
            x += M
        elif x > y:
            y += N
        else:
            ans = x
            break
    print(ans)