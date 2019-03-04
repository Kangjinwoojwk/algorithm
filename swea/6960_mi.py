T = int(input())
def sol(cnt, time):
    global ans
    global N
    if cnt > ans:
        ans = cnt
    for i in range(N):
        if chk[i] and time + S[i] <= F[i]:
            chk[i] = False
            sol(cnt + 1, time + S[i])
            chk[i] = True


for test_case in range(1, T + 1):
    N = int(input())
    S = [0 for _ in range(N)]
    F = [0 for _ in range(N)]
    chk = [True for _ in range(N)]
    ans = 0
    for i in range(N):
        S[i], F[i] = map(int, input().split())
    sol(0, 0)
    print('#{} {}'.format(test_case, ans))
