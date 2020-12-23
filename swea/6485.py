import sys
sys.stdin = open('6485.txt', 'r')
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    result = [0]*5001
    for i in range(N):
        a, b = map(int, input().split())
        for j in range(a, b + 1):
            result[j] += 1
    P = int(input())
    re = []
    for i in range(P):
        re.append(result[int(input())])
    print('#{}'.format(tc), ' '.join(map(str, re)))


# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     A = []
#     B = []
#     for _ in range(N):
#         a, b = map(int, input().split())
#         A.append(a)
#         B.append(b)
#     P = int(input())
#     C = []
#     result = []
#     for _ in range(P):
#         c = int(input())
#         C.append(c)
#         result.append(0)
#     for i in range(N):
#         for j in range(A[i], B[i] + 1):
#             for k in range(P):
#                 if j == C[k]:
#                     result[k] += 1
#     print('#{}'.format(tc), end='')
#     for i in result:
#         print(' {}'.format(i), end='')
#     print()