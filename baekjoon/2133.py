def tile(n):
    if ans[n] > 0:
        return ans[n]
    ans[n] = tile(n - 2) * 3
    for i in range(4, n + 1, 2):
        ans[n] += tile(n - i)*2
    return ans[n]


ans = [0] * 31
ans[0] = 1
ans[2] = ans[0] * 3
tile(30)
print(ans[int(input())])