def sol(n):
    global max_value, min_value
    if n == k:
        chk = ''.join(result)
        if chk > max_value:
            max_value = chk
        if chk < min_value:
            min_value = chk
        return
    if giho[n] == '<':
        for i in range(int(result[n]) + 1, 10):
            if visit[i]:
                visit[i] = False
                result[n + 1] = str(i)
                sol(n + 1)
                visit[i] = True
    if giho[n] == '>':
        for i in range(int(result[n])):
            if visit[i]:
                visit[i] = False
                result[n + 1] = str(i)
                sol(n + 1)
                visit[i] = True

k = int(input())
giho = input().split()
visit = [True] * 10
max_value = '0' * (k + 1)
min_value = '9' * (k + 1)
result = ['0'] * (k + 1)
for i in range(10):
    result[0] = str(i)
    visit[i] = False
    sol(0)
    visit[i] = True
print(max_value)
print(min_value)



# 다보는 브루트 포스는 시간 초과
# def sol(n):
#     global max_value, min_value
#     if n == k + 1:
#         for i in range(k):
#             if giho[i] == '<' and result[i] < result[i + 1]:
#                 continue
#             elif giho[i] == '>' and result[i] > result[i + 1]:
#                 continue
#             else:
#                 return
#         chk = ''.join(result)
#         if chk > max_value:
#             max_value = chk
#         if chk < min_value:
#             min_value = chk
#         return
#     for i in range(10):
#         if visit[i]:
#             visit[i] = False
#             result[n] = str(i)
#             sol(n + 1)
#             visit[i] = True
#
#
# k = int(input())
# giho = input().split()
# visit = [True] * 10
# max_value = '0' * (k + 1)
# min_value = '9' * (k + 1)
# result = ['0'] * (k + 1)
# sol(0)
# print(max_value)
# print(min_value)