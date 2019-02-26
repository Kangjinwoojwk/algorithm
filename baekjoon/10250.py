T = int(input())
for test_case in range(T):
    H, W, N = map(int, input().split())
    floor = N % H
    if floor == 0:
        floor = H
    ho = ((N - 1) // H) + 1
    ans = str(floor)
    if ho < 10:
        ans += '0' + str(ho)
    else:
        ans += str(ho)
    print(ans)