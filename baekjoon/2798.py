N, M = map(int, input().split())
cards = list(map(int, input().split()))
chk = [False] * N
cards.sort()
max_value = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            sum_value = cards[i] + cards[j] + cards[k]
            if max_value < sum_value <= M:
                max_value = sum_value
            if max_value == M:
                break
print(max_value)








# 정렬 후에 올라가면서 하는 것은 건너 뛰는 게 더 적합한 경우를 무시한다.
# cards.sort()
# max_value = 0
# for i in range(N - 2):
#     sum_value = cards[i] + cards[i + 1] + cards[i + 2]
#     if max_value < sum_value <= M:
#         max_value = sum_value
#     if sum_value > M:
#         break
#     if max_value == M:
#         break
# print(max_value)

# 전부 하는 것은 시간 초과가 난다.
# N, M = map(int, input().split())
# cards = list(map(int, input().split()))
# def sol(N, M):
#     max_value = 0
#     for i in range(1 << N):
#         cnt = 0
#         sum = 0
#         for j in range(N):
#             if i & 1 << j:
#                 cnt += 1
#                 sum += cards[j]
#         if cnt != 3:
#             continue
#         if max_value < sum <= M:
#             max_value = sum
#         if max_value == M:
#             break
#     return max_value
# print(sol(N,M))