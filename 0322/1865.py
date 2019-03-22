import sys
sys.stdin = open('1865.txt', 'r')
def sol(n, chk):
    global N, ans
    if chk <= ans:
        return
    if n == N:
        ans = chk
        return
    for i in range(N):
        if take[i]:
            take[i] = False
            sol(n + 1, chk * (data[n][i]/100))
            take[i] = True
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    take = [True] * N
    ans = 0.0
    sol(0, 1.0)
    ans *= 100
    print('#{} {}'.format(tc, format(ans,'.6f')))



# def sol(n):
#     global N, ans
#     if n == N:
#         chk = 1.0
#         for i in range(N):
#             chk *= (data[i][work[i]]/100)
#         if chk > ans:
#             ans = chk
#         return
#     for i in range(N):
#         if visit[i]:
#             visit[i] = False
#             work.append(i)
#             sol(n + 1)
#             work.pop()
#             visit[i] = True
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     data = [list(map(int, input().split())) for _ in range(N)]
#     visit = [True] * N
#     work = list()
#     ans = 0.0
#     sol(0)
#     ans *= 100
#     print('#{} {}'.format(tc, ans))