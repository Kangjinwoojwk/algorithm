N, M, T, K = map(int, input().split())
X = []
Y = []
for _ in range(T):
    A, B = map(int, input().split())
    X.append(A)
    Y.append(B)
max_dia = 0
X_Y = []








# 무슨 생각일까...보석으로 부터 증가 방향만 세는 것은...
# for i in range(T):
#     cnt = 1
#     max_y = 0
#     for j in range(T):
#         if i == j:
#             continue
#         x, y = X[j] - X[i], Y[j] - Y[i]
#         if 0 <= x <= K and 0 <= y <= K:
#             cnt += 1
#             if y > max_y:
#                 max_y = y
#     if cnt > max_dia:
#         max_dia = cnt
#         X_Y = [X[i], Y[i] + max_y]
# print(X_Y[0], X_Y[1])
# print(max_dia)


# 이번엔 시간 초과다!!!
# N, M, T, K = map(int, input().split())
# X = []
# Y = []
# for _ in range(T):
#     A, B = map(int, input().split())
#     X.append(A)
#     Y.append(B)
# max_dia = 0
# X_Y = []
# for i in range(N - K + 1):
#     for j in range(M - K + 1):
#         cnt = 0
#         for k in range(T):
#             if i <= X[k] <= i + K and j <= Y[k] <= j + K:
#                 cnt += 1
#         if cnt > max_dia:
#             max_dia = cnt
#             X_Y = [i, j]
# print(X_Y[0], X_Y[1] + K)
# print(max_dia)


# 메모리 초과
# N, M, T, K = map(int, input().split())
# dia = {}
# max_v = 0
# for _ in range(T):
#     A, B = map(int, input().split())
#     for i in range(K + 1):
#         for j in range(K + 1):
#             if B - j >= 0 and A - i >= 0:
#                 if (B - j, A - i) not in dia:
#                     dia[(B - j, A - i)] = 1
#                 else:
#                     dia[(B - j, A - i)] += 1
#                 if dia[(B - j, A - i)] > max_v:
#                     max_v = dia[(B - j, A - i)]
# for k, v in dia.items():
#     if v == max_v:
#         print(k[0], k[1] + K)
#         break
# print(max_v)