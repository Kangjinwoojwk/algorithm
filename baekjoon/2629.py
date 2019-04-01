N = int(input())
li = list(map(int, input().split()))
ans = [False] * 80001
Q = list()
Q.append(0)
ans[0] = True
for i in range(N):
    for j in range(len(Q)):
        if ans[Q[j] + li[i]] == False:
            Q.append(Q[j] + li[i])
            ans[Q[j] + li[i]] = True
        if ans[Q[j] - li[i]] == False:
            Q.append(Q[j] - li[i])
            ans[Q[j] - li[i]] = True
M = int(input())
get = list(map(int, input().split()))
print(' '.join(['Y' if ans[i] else 'N' for i in get]))