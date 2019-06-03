

for tc in range(1, int(input()) + 1):
    N = int(input())
    choo = list(map(int, input().split()))
    choo.sort()
    used = [False for _ in range(N)]
    ans = 0







# 시간초과
# def sol(n, left, right):
#     global ans
#     if n == N:
#         ans += 1
#         return
#     for i in range(N):
#         if visit[i]:
#             visit[i] = False
#             sol(n + 1, left + li[i], right)
#             if right + li[i] <= left:
#                 sol(n + 1, left, right + li[i])
#             visit[i] = True
#
# result = list()
# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     li = list(map(int, input().split()))
#     visit = [True] * N
#     ans = 0
#     sol(0, 0, 0)
#     result.append('#{} {}'.format(tc, ans))
# print('\n'.join(result))