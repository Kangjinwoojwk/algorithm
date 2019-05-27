from collections import deque
N, K = map(int, input().split())
Q = deque()
li = [[-1] * 500001 for _ in range(2)]
Q.append(N)
li[0][N] = 0
step = 1
while Q:
    for i in range(len(Q)):
        x = Q.popleft()
        if x * 2 <= 500000 and li[step % 2][x * 2] == -1:
            li[step % 2][x * 2] = step
            Q.append(x * 2)
        if x + 1 <= 500000 and li[step % 2][x + 1] == -1:
            li[step % 2][x + 1] = step
            Q.append(x + 1)
        if x - 1 > 0 and li[step % 2][x - 1] == -1:
            li[step % 2][x - 1] = step
            Q.append(x - 1)
    step += 1
step = 0
while K <= 500000:
    if li[step % 2][K] <= step:
        print(step)
        exit()
    step += 1
    K += step
print(-1)








# from collections import deque
# N, K = map(int, input().split())
# Q = deque()
# ans = True
# Q.append(N)
# i = 1
# while K not in Q:
#     for _ in range(len(Q)):
#         temp = Q.popleft()
#         if 2 * temp <= 500000:
#             Q.append(2 * temp)
#         if temp - 1 >= 0:
#             Q.append(temp - 1)
#         if temp + 1 <= 500000:
#             Q.append(temp + 1)
#     K += i
#     i += 1
#     if K > 500000:
#         ans = False
#         break
# if ans:
#     print(i - 1)
# else:
#     print(-1)