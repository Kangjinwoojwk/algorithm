def sol(n, start, end):
    if start >= end:
        return
    N = (start + end)//2
    if li[N] == data[n]:
        result[n] = di[li[N]]
        return
    elif li[N] < data[n]:
        sol(n, N + 1, end)
    else:
        sol(n, start, N)
N = int(input())
li = list(map(int, input().split()))
di = {}
for i in li:
    if i in di:
        di[i] += 1
    else:
        di[i] = 1
li = list(set(li))
li.sort()
N = len(li)
M = int(input())
data = list(map(int, input().split()))
result = [0] * M
for i in range(M):
    sol(i, 0, N)
print(' '.join(map(str, result)))