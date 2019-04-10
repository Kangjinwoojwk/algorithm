n = int(input())
it = 1
for i in range(n - 1):
    it += 4
n = it
it = 0
li = [[' '] * n for _ in range(n)]
while it <= (n // 2):
    for i in range(it, n - it):
        li[it][i] = '*'
        li[n - it - 1][i] = '*'
        li[i][it] = '*'
        li[i][n - it - 1] = '*'
    it += 2
for i in range(n):
    print(''.join(li[i]))