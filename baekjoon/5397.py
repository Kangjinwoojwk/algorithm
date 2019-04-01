for _ in range(int(input())):
    get = input()
    st = [[], []]
    for i in get:
        if i == '-':
            if st[0]:
                st[0].pop()
        elif i == '<':
            if st[0]:
                st[1].append(st[0].pop())
        elif i == '>':
            if st[1]:
                st[0].append(st[1].pop())
        else:
            st[0].append(i)
    print(''.join(st[0]) + ''.join(st[1][::-1]))




# 답은 나오지만 시간초과...후...좀더 슈웨이한 방법이 필요하다
# import sys
# for _ in range(int(sys.stdin.readline().rstrip())):
#     get = sys.stdin.readline().rstrip()
#     ans =[]
#     idx = -1
#     for i in get:
#         if i == '-':
#             if idx != -1:
#                 ans.pop(idx)
#                 idx -= 1
#         elif i == '>':
#             if idx < len(ans) - 1:
#                 idx += 1
#         elif i == '<':
#             if idx > -1:
#                 idx -= 1
#         else:
#             ans[idx + 1:idx + 1] = i
#             idx += 1
#     print(''.join(ans))