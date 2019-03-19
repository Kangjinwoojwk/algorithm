N = int(input())
li = [1, 5, 10, 50]
que = [1, 5, 10, 50]
for i in range(1, N):
    for j in range(len(que)):
        temp = que.pop(0)
        for k in li:
            que.append(temp + k)
    que = list(set(que))
print(len(que))