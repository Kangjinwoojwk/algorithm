for tc in range(1, int(input()) + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    data.sort(key=lambda x: (x[0] - 1)/x[1], reverse=True)
    ans = 1
    for i in data:
        ans = ans * i[0] + i[1]
    print('#{} [}'.format(tc,ans))




# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     data = [list(map(int, input().split()))for _ in range(N)]
#     ans = [[data[i][0] + data[i][1] if i == j else 0 for i in range(N)]for j in range(N)]
#     i, j = 0, 1
#     while j - i != N:
#         ans[i][j] = min(ans[i][j - 1] * data[j][0] + data[j][1], ans[i + 1][j] * data[i][0] + data[i][1])
#         i += 1
#         j += 1
#         if j == N:
#             temp = j - i
#             i = 0
#             j = temp + 1
#     print('#{} {}'.format(tc, ans[0][N - 1]))
