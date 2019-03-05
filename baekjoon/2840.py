N, K = map(int, input().split())
li = ['?' for _ in range(N)]
v = 0
chk = True
for _ in range(K):
    n, d = input().split()
    v = (v - int(n)) % N
    if li[v] != d and li[v] != '?':
        chk = False
        break
    if d in li[:v]+li[v+1:]:
        chk = False
        break
    li[v] = d
if chk:
    print(''.join(li[v:]+li[:v]))
else:
    print('!')
