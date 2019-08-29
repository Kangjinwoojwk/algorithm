cnt = [[0] * 31 for i in range(31)]
cnt[0][0] = 1
def sol(W, H):
    if cnt[W][H]:
        return cnt[W][H]
    if W:
        cnt[W][H] += sol(W - 1, H + 1)
    if H:
        cnt[W][H] += sol(W, H - 1)
    return cnt[W][H]
sol(30, 0)
while True:
    N = int(input())
    if N == 0:
        break
    print(cnt[N][0])