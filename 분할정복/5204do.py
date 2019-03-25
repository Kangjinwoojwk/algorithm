# def merge(li):
#     global cnt
#     n = len(li)
#     if n == 1:
#         return li
#     L = merge(li[:n//2])
#     R = merge(li[n//2:])
#     result = []
#     while L and R:
#         if L[0] <= R[0]:
#             result.append(L.pop(0))
#         else:
#             result.append(R.pop(0))
#     if L:
#         result.extend(L)
#         cnt += 1
#     else:
#         result.extend(R)
#     return result

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cnt = 0
    li = list(map(int, input().split()))
    st = list()

    print('#{} {} {}'.format(tc, li[N//2], cnt))