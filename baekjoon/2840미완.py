N, K = map(int, input().split())
li = ['' for _ in range(N)]
v = N - 1
chk = True
for _ in range(K):
    n, d = input().split()
    n = int(n)
    if _ == 0:
        li[v] = d
    else:
        v = (v - n) % N
        if li[v] != '':
            chk = False
            break
        li[v] = d
li = [li[i] if li[i] != '' else '!' for i in range(N)]
li = li[1:] + [li[0]]
if chk:
    print(''.join(li))
else:
    print('!')