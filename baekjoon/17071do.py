from collections import deque
N, K = map(int, input().split())
Q = deque()
ans = True
Q.append(N)
i = 1
while K not in Q:
    for _ in range(len(Q)):
        temp = Q.popleft()
        if 2 * temp <= 500000:
            Q.append(2 * temp)
        if temp - 1 >= 0:
            Q.append(temp - 1)
        if temp + 1 <= 500000:
            Q.append(temp + 1)
    K += i
    i += 1
    if K > 500000:
        ans = False
        break
if ans:
    print(i - 1)
else:
    print(-1)