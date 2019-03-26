def sol(n, cnt):
    global N, ans
    if cnt == N // 2:
        value = 0
        for i in range(N):
            for j in range(N):
                if visit[i] and visit[j]:
                    value += data[i][j]
                if visit[i] == visit[j] == False:
                    value -= data[i][j]
        value = abs(value)
        if ans > value:
            ans = value
        return
    if N - n < N//2 - cnt:
        return
    sol(n + 1, cnt)
    visit[n] = True
    sol(n + 1, cnt + 1)
    visit[n] = False


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
visit = [True] * N
ans = 2 ** 30
sol(0, 0)
print(ans)

# def cal():
#     global ans, N
#     value = 0
#     for i in range(N):
#         for j in range(N):
#             if visit[i] == visit[j] == True:
#                 value += data[i][j]
#             elif visit[i] == visit[j] == False:
#                 value -= data[i][j]
#     value = abs(value)
#     if value < ans:
#         ans = value
#
# def sol(n, cnt):
#     global N
#     if cnt == N // 2:
#         cal()
#         return
#     if n == N:
#         return
#     visit[n] = False
#     sol(n + 1, cnt + 1)
#     visit[n] = True
#     sol(n + 1, cnt)
#
#
# N = int(input())
# data = [list(map(int, input().split())) for _ in range(N)]
# visit = [True] * N
# ans = 2 ** 30
# sol(0, 0)
# print(ans)