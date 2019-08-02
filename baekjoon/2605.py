N = int(input())
data = list(map(int, input().split()))
ans = list()
for i in range(N):
    ans.insert(len(ans) - data[i], i + 1)
print(' '.join(map(str, ans)))