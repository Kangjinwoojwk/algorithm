# 중복이 장난 아니였다. 해결....
def cal(n):
    global ans
    check = [_ for _ in range(N)]
    for i in range(H):
        for j in range(N - 1):
            if sero[i][j]:
                check[j], check[j + 1] = check[j + 1], check[j]
    if check == number:
        ans = n


def sol(x, y, n, chk):
    if ans != -1:
        return
    if chk == 0:
        cal(n)
        return
    for j in range(y + 1, N - 1):
        if sero[x][j] or (j - 1 >= 0 and sero[x][j - 1]) or (j + 1 < N - 1 and sero[x][j + 1]):
            continue
        sero[x][j] = True
        sol(x, j, n, chk - 1)
        sero[x][j] = False
    for i in range(x + 1, H):
        for j in range(N - 1):
            if sero[i][j] or (j - 1 >= 0 and sero[i][j - 1]) or (j + 1 < N - 1 and sero[i][j + 1]):
                continue
            sero[i][j] = True
            sol(i, j, n, chk - 1)
            sero[i][j] = False


N, M, H = map(int, input().split())
number = [_ for _ in range(N)]
sero = [[False]*(N - 1) for _ in range(H)]
ans = -1
for _ in range(M):
    a, b = map(int, input().split())
    sero[a - 1][b - 1] = True
cal(0)
for modify in range(1, 4):
    if ans != -1:
        break
    sol(0, 0, modify, modify)
print(ans)



# 시간 초과 재귀가 아닌 방법을 써봐야할까? 연산을 줄일 방법은 없을까?
# 이런 3 넘는건 안나온다는걸 안봤다....문제를 똑바로 읽자
# def cal(n):
#     global ans
#     check = [_ for _ in range(N)]
#     for i in range(H):
#         for j in range(N - 1):
#             if sero[i][j]:
#                 check[j], check[j + 1] = check[j + 1], check[j]
#     if check == number and n < ans:
#         ans = n
#
# def sol(x, y, n):
#     if n >= ans:
#         return
#     if x == H:
#         cal(n)
#         return
#     if y == N - 2:
#         sol(x + 1, 0, n)
#     else:
#         sol(x, y + 1, n)
#     if not sero[x][y]:
#         if y == 0:
#             if N == 2:
#                 sero[x][y] = True
#                 sol(x + 1, 0, n + 1)
#                 sero[x][y] = False
#             else:
#                 if not sero[x][y + 1]:
#                     sero[x][y] = True
#                     sol(x, y + 1, n + 1)
#                     sero[x][y] = False
#         elif y == N - 2:
#             if not sero[x][y - 1]:
#                 sero[x][y] = True
#                 sol(x + 1, 0, n + 1)
#                 sero[x][y] = False
#         else:
#             if not sero[x][y - 1] and not sero[x][y + 1]:
#                 sero[x][y] = True
#                 sol(x, y + 1, n + 1)
#                 sero[x][y] = False
#
#
# N, M, H = map(int, input().split())
# number = [_ for _ in range(N)]
# sero = [[False]*(N - 1) for _ in range(H)]
# ans = N * H
# for _ in range(M):
#     a, b = map(int, input().split())
#     sero[a - 1][b - 1] = True
# sol(0, 0, 0)
# if ans == N * H:
#     ans = -1
# print(ans)