for tc in range(1, int(input()) + 1):
    N, O, M = map(int, input().split())
    num = list(map(int, input().split()))
    cal = list(map(int, input().split()))
    visit = [0] * 1000
    get = int(input())
    Q = list()
    for i in range(1000):
        a = str(i)
        for j in a:
            if int(j) not in num:
                break
        else:
            Q.append(i)
            visit[i] = len(a)
    number = Q[:]
    while Q:
        n = Q.pop(0)
        for i in number:
            cnt = visit[i] + visit[n] + 1
            if cnt >= M:
                continue
            for j in cal:
                if j == 1:
                    temp = n + i
                    if 0 <= temp < 1000 and (visit[temp] == 0 or visit[temp] > cnt):
                        visit[temp] = cnt
                        Q.append(temp)
                if j == 2:
                    temp = n - i
                    if 0 <= temp < 1000 and (visit[temp] == 0 or visit[temp] > cnt):
                        visit[temp] = cnt
                        Q.append(temp)
                if j == 3:
                    temp = n * i
                    if 0 <= temp < 1000 and (visit[temp] == 0 or visit[temp] > cnt):
                        visit[temp] = cnt
                        Q.append(temp)
                if j == 4 and i != 0:
                    temp = n // i
                    if 0 <= temp < 1000 and (visit[temp] == 0 or visit[temp] > cnt):
                        visit[temp] = cnt
                        Q.append(temp)
    if get in number:
        ans = visit[get]
    elif visit[get]:
        ans = visit[get] + 1
    else:
        ans = -1
    print('#%d %d' % (tc, ans))



# 후...BFS도 실패
# for tc in range(1, int(input()) + 1):
#     N, O, M = map(int, input().split())
#     num = list(map(int, input().split()))
#     cal = list(map(int, input().split()))
#     visit = [True] * 1000
#     get = input()
#     ans = M + 1
#     for i in get:
#         if int(i) not in num:
#             break
#     else:
#         ans = len(get)
#     if ans != len(get):
#         get = int(get)
#         cnt = 0
#         Q = list()
#         for i in num:
#             Q.append((i, 0, 0))
#             visit[i] = False
#         while cnt <= M:
#             cnt += 1
#             for _ in range(len(Q)):
#                 re, st, gi = Q.pop(0)
#                 if re < 0 or re > 999 or st < 0 or st > 999:
#                     continue
#                 if re == get:
#                     ans = cnt
#                     cnt = M + 1
#                     break
#                 if gi == 0:
#                     for i in num:
#                         if 0 <= 10 * re + i < 1000:
#                             if visit[10 * re + i]:
#                                 visit[10 * re + i] = False
#                                 Q.append((10 * re + i, st, gi))
#                     for i in cal:
#                         Q.append((re, st, i))
#                 else:
#                     for i in num:
#                         Q.append((re, 10 * st + i, gi))
#                     if st:
#                         if gi == 1:
#                             re += st
#                         elif gi == 2:
#                             re -= st
#                         elif gi == 3:
#                             re *= st
#                         elif gi == 4:
#                             re //= st
#                         for i in cal:
#                             if 0 <= re < 1000:
#                                 if visit[re]:
#                                     visit[re] = False
#                                     Q.append((re, 0, i))
# 
#     if ans == M + 1:
#         ans = -1
#     print('#%d %d' % (tc, ans))


# 시간 초과...BFS해야 하나 보다
# def sol(re, st, gi, cnt):
#     global ans
#     if cnt >= ans:
#         return
#     elif re == int(get):
#         ans = cnt
#         return
#     if re < 0 or re > 999 or st < 0 or st > 999:
#         return
#     if gi == 0:
#         for i in num:
#             sol(10 * re + i, st, gi, cnt + 1)
#         for i in cal:
#             sol(re, st, i, cnt + 1)
#     else:
#         for i in num:
#             sol(re, 10 * st + i, gi, cnt + 1)
#         if st:
#             if gi == 1:
#                 re = re + st
#             elif gi == 2:
#                 re = re - st
#             elif gi == 3:
#                 re = re * st
#             elif gi == 4:
#                 re = re // st
#             for i in cal:
#                 sol(re, 0, i, cnt + 1)
#
# for tc in range(1, int(input()) + 1):
#     N, O, M = map(int, input().split())
#     num = list(map(int, input().split()))
#     cal = list(map(int, input().split()))
#     get = input()
#     ans = M + 1
#     for i in get:
#         if int(i) not in num:
#             break
#     else:
#         ans = len(get)
#     if ans != len(get):
#         for i in num:
#             if i == 0:
#                 continue
#             sol(int(i), 0, 0, 1)
#     if ans == M + 1:
#         ans = -1
#     print('#%d %d' % (tc, ans))

# def calc(string):
#     n1 = ''
#     n2 = ''
#     ca = ''
#     for i in string:
#         if i in giho and ca == '':
#             ca = i
#         elif i in giho:
#             if ca == '+':
#                 n1 = str(int(n1) + int(n2))
#             elif ca == '-':
#                 n1 = str(int(n1) - int(n2))
#             elif ca == '*':
#                 n1 = str(int(n1) * int(n2))
#             elif ca == '/':
#                 n1 = str(int(n1) // int(n2))
#             n2 = ''
#             ca = i
#             if ca == '=':
#                 break
#         elif ca == '':
#             n1 += i
#         else:
#             n2 += i
#     return n1
#
#
# def sol(result, cnt):
#     global ans
#     if cnt >= ans:
#         return
#     elif result[-1] == '=':
#         a = calc(result)
#         if a == int(get):
#             ans = cnt
#         return
#     for i in num:
#         if result[-1] in giho and i == '0':
#             continue
#         sol(result + i, cnt + 1)
#     for i in cal:
#         if i == 1:
#             sol(result + '+', cnt + 1)
#         elif i == 2:
#             sol(result + '-', cnt + 1)
#         elif i == 3:
#             sol(result + '*', cnt + 1)
#         elif i == 4:
#             sol(result + '/', cnt + 1)
#         elif i == 5:
#             sol(result + '=', cnt + 1)
#
# for tc in range(1, int(input()) + 1):
#     N, O, M = map(int, input().split())
#     num = input().split()
#     cal = set(map(int, input().split()))
#     cal.add(5)
#     giho = {'+', '-', '*', '/', '='}
#     get = input()
#     ans = M
#     for i in get:
#         if i not in num:
#             break
#     else:
#         ans = len(get)
#     if ans != len(get):
#         for i in num:
#             if i == '0':
#                 continue
#             else:
#                 sol(i, 1)
#     print(ans)



# 다시짜자
# def sol(result, cnt):
#     global ans
#     if int(result) < 0 or int(result) > 999:
#         return
#     if cnt >= ans:
#         return
#     elif result == get:
#         ans = cnt
#         return
#     for i in num:
#         sol(result + i, cnt + 1)
#         for j in cal:
#             if j == 1:
#                 sol(str(int(result) + int(i)), cnt + 2)
#             elif j == 2:
#                 sol(str(int(result) - int(i)), cnt + 2)
#             elif j == 3:
#                 sol(str(int(result) * int(i)), cnt + 2)
#             elif j == 4:
#                 if i != '0':
#                     sol(str(int(result) // int(i)), cnt + 2)
#
#
# for tc in range(1, int(input()) + 1):
#     N, O, M = map(int, input().split())
#     num = input().split()
#     cal = set(map(int, input().split()))
#     get = input()
#     ans = M
#     for i in num:
#         if i == '0':
#             continue
#         sol(i, 1)
#     if ans == M:
#         ans = -1
#     else:
#         ans += 1
#     print(ans)
