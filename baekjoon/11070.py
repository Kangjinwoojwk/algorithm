for tc in range(int(input())):
    n, m = map(int, input().split())
    S = [0] * n
    A = [0] * n
    for _ in range(m):
        a, b, p, q = map(int, input().split())
        S[a - 1] += p
        A[a - 1] += q
        S[b - 1] += q
        A[b - 1] += p
    ans = [(1000 * (S[i] ** 2))//((S[i] ** 2) + (A[i] ** 2)) if ((S[i] ** 2) + (A[i] ** 2)) else 0 for i in range(n)]
    print(max(ans))
    print(min(ans))