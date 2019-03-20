from collections import deque
su, do = map(int, input().split())
Q = deque()
Q.append(su)
time = -1
cnt = 0
visit = [True]*100001
while Q:
    if cnt:
        break
    time += 1
    for i in range(len(Q)):
        temp = Q.popleft()
        if temp == do:
            cnt += 1
            continue
        visit[temp] = False
        if temp - 1 >= 0 and visit[temp - 1]:
            Q.append(temp - 1)
        if temp + 1 <= 100000 and visit[temp + 1]:
            Q.append(temp + 1)
        if temp * 2 <= 100000 and visit[temp * 2]:
            Q.append(temp * 2)
print(time)
print(cnt)

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