from collections import deque
N = int(input())
ans = 0
Q = deque()
Q.append(N)
while 1 not in Q:
    ans += 1
    for _ in range(len(Q)):
        temp = Q.popleft()
        if temp % 3 == 0:
            Q.append(temp // 3)
        if temp % 2 == 0:
            Q.append(temp // 2)
        Q.append(temp - 1)
print(ans)