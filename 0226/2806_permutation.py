def permutation_sol(cnt):
    global N
    global ans
    if cnt == N:
        it = True
        for i in range(N):
            for j in range(N):
                if i != j:
                    if i - j == li_pair[i] - li_pair[j] or i - j == -(li_pair[i] - li_pair[j]):
                        it = False
        if it:
            ans += 1
    for i in range(N):
        if li_use[i]:
            li_pair[cnt] = i
            li_use[i] = False
            permutation_sol(cnt + 1)
            li_use[i] = True

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    ans = 0
    li_pair = [0] * N
    li_use = [True] * N
    ans = 0
    permutation_sol(0)
    print('#{} {}'.format(test_case, ans))
