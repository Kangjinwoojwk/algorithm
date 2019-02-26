T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    S = [0 for _ in range(N)]
    F = [0 for _ in range(N)]
    for i in range(N):
        S[i], F[i] = map(int, input().split())
    # cha = [F[i] - S[i] for i in range(N) if F[i] - S[i] > 0]
    t = 0
