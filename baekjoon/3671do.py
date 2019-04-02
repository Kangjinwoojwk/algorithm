import time
a = time.time()
ceh = [True] * 10000000
ceh[0] = ceh[1] = False
for i in range(2, 3164):
    if ceh[i] == False:
        continue
    for j in range(2 * i, 10000000, i):
        ceh[j] = False
print(time.time() - a)
def sol(it):
    global ans
    temp = int(it)
    if ceh[temp]:
        if visit2[temp]:
            visit2[temp] = False
            ans += 1
    for k in range(N):
        if visit[k] == False:
            continue
        visit[k] = False
        sol(it + get[k])
        visit[k] = True
result = list()
for _ in range(int(input())):
    get = input()
    N = len(get)
    visit = [True] * N
    visit2 = [True] * 10000000
    ans = 0
    for i in range(N):
        visit[i] = False
        sol(get[i])
        visit[i] = True
    result.append(ans)
print('\n'.join(map(str, result)))
print(time.time() - a)






# ceh = [True] * 10000000
# i = 2
# ceh[0] = ceh[1] = False
# while i * i < 10000000:
#     if ceh[i] == False:
#         i += 1
#         continue
#     j = 2 * i
#     while j < 10000000:
#         ceh[j] = False
#         j += i
#     i += 1
# def sol(n, it):
#     global ans
#     if n == 0:
#         if ceh[it] and visit2[it]:
#             visit2[it] = False
#             ans += 1
#         return
#     i = n % 10
#
# for _ in range(int(input())):
#     get = int(input())
#     visit2 = [True] * 10000000
#     ans = 0
#     sol(get, 0)
#     print(ans)



# ceh = [True] * 10000000
# i = 2
# ceh[0] = ceh[1] = False
# while i * i < 10000000:
#     if ceh[i] == False:
#         i += 1
#         continue
#     j = 2 * i
#     while j < 10000000:
#         ceh[j] = False
#         j += i
#     i += 1
# def sol(n, it):
#     global ans
#     i = int(it)
#     if ceh[i]:
#         result.add(i)
#     if n == N:
#         return
#     for j in range(N):
#         if visit[j]:
#             visit[j] = False
#             sol(n + 1, it + get[j])
#             visit[j] = True
#     sol(n + 1, it)
# ans = []
# for _ in range(int(input())):
#     get = input()
#     N = len(get)
#     visit = [True] * N
#     result = set()
#     sol(0, '0')
#     ans.append(str(len(result)))
# print('\n'.join(ans))