from collections import deque
su, do = map(int, input().split())
Q = deque()
Q.append(su)
time = 0
visit = [True] * 100001
visit[su] = False
while True:
    if visit[do] == False:
        break
    for i in range(len(Q)):
        temp = Q.popleft()
        if temp - 1 >= 0 and visit[temp - 1]:
            visit[temp - 1] = False
            Q.append(temp - 1)
        if temp + 1 <= 100000 and visit[temp + 1]:
            visit[temp + 1] = False
            Q.append(temp + 1)
        if temp * 2 <= 100000 and visit[temp * 2]:
            visit[temp * 2] = False
            Q.append(temp * 2)
    time += 1
print(time)