from collections import deque
N, K = map(int, input().split())
step = 1
su = deque()
su.append(N)
while K not in su:
    for i in range(len(su)):
        temp = su.popleft()
        if temp - 1 >= 0:
            su.append(temp - 1)
        if temp + 1 <= 500000:
            su.append(temp + 1)
        if temp * 2 <= 500000:
            su.append(temp * 2)
    K += step
    step += 1
    if K > 500000:
        break
if K > 500000:
    print(-1)
else:
    print(step - 1)