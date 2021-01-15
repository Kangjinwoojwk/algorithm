for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    coin = [list(map(int, input().split())) for _ in range(N)]
    cnt, price = 0, 0
    
    print('#{} {} {}'.format(tc, cnt, price))


# 시간 초과
# for tc in range(1, int(input()) + 1):
#     N, K = map(int, input().split())
#     coin = [list(map(int, input().split())) for _ in range(N)]
#     cnt, price = 0, 0
#     def sol(pri):
#         temp_coin = [coin[j][:] for j in range(N)]
#         ptr = N - 1
#         while pri:
#             if temp_coin[ptr][0] <= pri:
#                 pri -= temp_coin[ptr][0] * (pri // temp_coin[ptr][0])
#                 temp_coin[ptr][1] = 1
#                 ptr -= 1
#             else:
#                 ptr -= 1
#         return len([0 for j in range(N) if temp_coin[j][1] == 1 and coin[j][1] != 1])
#     for i in range(K - 1, 0, - 1):
#         temp_cnt = sol(K - i)
#         if temp_cnt > cnt:
#             cnt = temp_cnt
#             price = i
#     print('#{} {} {}'.format(tc, cnt, price))