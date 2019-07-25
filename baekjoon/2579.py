N = int(input())
data = [[int(input()), 0] for _ in range(N)]
for i in range(1, N):
    data[i][1] = data[i][0] + data[i - 1][0]
    if i == 1:
        continue
    data[i][0] = max(data[i - 2]) + data[i][0]
print(max(data[-1]))



# dfs는 시간이 너무 많이 걸린다. dp로 해야 하나...
# def sol(now, step, score):
#     global ans
#     if now == N:
#         if ans < score:
#             ans = score
#         return
#     if step < 1:
#         sol(now + 1, step + 1, score + data[now + 1])
#     if now + 2 > N:
#         return
#     sol(now + 2, 0, score+data[now + 2])
#
#
# N = int(input())
# data = [int(input()) for _ in range(N)]
# data.insert(0, 0)
# ans = 0
# sol(0, -1, 0)
# print(ans)