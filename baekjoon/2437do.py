from collections import deque
N = int(input())
choo = list(map(int, input().split()))
choo.sort()
weight = [True] * choo[-1] * N
Q = deque()
Q.append(0)
weight[0] = False
n = 0
while n < N:
    for _ in range(len(Q)):
        temp = Q.popleft()
        Q.append(temp)
        temp += choo[n]
        if weight[temp]:
            weight[temp] = False
            Q.append(temp)
    n += 1
n = 0
while n < 1000000000:
    if weight[n]:
        print(n)
        break
    n += 1