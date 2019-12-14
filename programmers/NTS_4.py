# 참고 자료 https://oeis.org/A144084
def solution(n, k):
    if k > n:
        return 0
    answer = 1
    for i in range(1, n + 1):
        answer *= i
    for i in range(1, k + 1):
        answer //= i
    for i in range(1, n - k + 1):
        answer //= i
    answer = answer ** 2
    for i in range(1, k + 1):
        answer *= i
    return answer % 10007



# def solution(n, k):
#     answer = [0]
#     pann = [[True] * n for i in range(n)]
#     def sol(cnt, line):
#         if cnt == 0:
#             answer[0] += 1
#         for i in range(line, n):
#             for j in range(n):
#                 if pann[i][j]:
#                     for k in range(i + 1, n):
#                         pann[k][j] = False
#                     sol(cnt - 1, i + 1)
#                     for k in range(i + 1, n):
#                         pann[k][j] = True
#     sol(k, 0)
#     return answer[0] % 10007
#
# print(solution(6,2))