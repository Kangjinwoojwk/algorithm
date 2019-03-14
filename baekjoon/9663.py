# li [0, 0,  ]
dx = [1, 1, 1]
dy = [-1, 0, 1]
def sol(n):
    global N, ans
    if n == N:
        ans += 1
        return
    li = []
    for i in range(N):
        if chess[n][i] == True:
            for j in range(1, N):
                for k in range(3):
                    x, y = n + j * dx[k], i + j * dy[k]
                    if 0 <= x < N and 0 <= y < N and chess[x][y]:
                        li.append([x, y])
                        chess[x][y] = False
            sol(n + 1)
            for j in li:
                chess[j[0]][j[1]] = True

N = int(input())
chess = [[True] * N for _ in range(N)]
ans = 0
sol(0)
print(ans)



# 판 계속 만들면 시간 초과....15는 심하다...
# dx = [1, 1, 1, 0, 0, -1, -1, -1]
# dy = [1, -1, 0, 1, -1, 0, -1, 1]
# def get_queen(n, x, y):
#     global N
#     for i in range(N):
#         for j in range(8):
#             get_x, get_y = x + i * dx[j], y + i * dy[j]
#             if 0 <= get_x < N and 0 <= get_y < N:
#                 chess[n][get_x][get_y] = False
#
#
# def sol(n):
#     global N, ans
#     if n == N:
#         ans += 1
#         return
#     for i in range(N):
#         if chess[n][n][i]:
#             chess[n + 1] = [chess[n][j][:] for j in range(N)]
#             get_queen(n + 1, n, i)
#             sol(n + 1)
#
# N = int(input())
# ans = 0
# chess = [[[True] * N for _ in range(N)]for __ in range(N + 1)]
# sol(0)
# print(ans)