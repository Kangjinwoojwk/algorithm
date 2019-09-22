def sol(n):
    if n == N - 1:
        ans.append(''.join(data))
        return
    for i in range(n, N):
        data[n], data[i] = data[i], data[n]
        sol(n + 1)
        data[n], data[i] = data[i], data[n]
data = input().split()
k = int(input())
ans = list()
N = len(data)
sol(0)
ans.sort()
print(ans[k - 1])