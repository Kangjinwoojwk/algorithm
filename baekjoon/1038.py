from collections import deque
li = [i for i in range(10)]
que = deque()
for i in range(10):
    que.append(i)
while que:
    for i in range(len(que)):
        x = que.popleft()
        for i in range(x % 10):
            li.append(x * 10 + i)
            que.append(x * 10 + i)
N = int(input())
if N < len(li):
    print(li[N])
else:
    print(-1)