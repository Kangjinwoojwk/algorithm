from collections import deque
su, do = map(int, input().split())
Q = deque()
Q.append(su)
time = 0
visit = [0] * 100001
while True:
    if visit[do]:
        break
    for i in range(len(Q)):
        temp = Q.popleft()
        if temp - 1 >= 0:
            visit[temp - 1] += 1
            Q.append(temp - 1)
        if temp + 1 <= 100000:
            visit[temp + 1] += 1
            Q.append(temp + 1)
        if temp * 2 <= 100000:
            visit[temp * 2] += 1
            Q.append(temp * 2)
    time += 1
print(time)
print(visit[do])

# from collections import deque
# su, do = map(int, input().split())
# Q = deque()
# Q.append(su)
# time = 0
# while True:
#     if do in Q:
#         break
#     for i in range(len(Q)):
#         temp = Q.popleft()
#         if temp - 1 >= 0:
#             Q.append(temp - 1)
#         if temp + 1 <= 100000:
#             Q.append(temp + 1)
#         if temp * 2 <= 100000:
#             Q.append(temp * 2)
#     time += 1
# print(time)
# print(Q.count(do))