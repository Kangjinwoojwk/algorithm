N = int(input())
ans = list(input())
l = len(ans)
for _ in range(N - 1):
    get = list(input())
    for i in range(l):
        if ans[i] != get[i]:
            ans[i] = '?'
print(''.join(ans))
