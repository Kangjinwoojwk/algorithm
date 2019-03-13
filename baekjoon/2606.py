def virus(n):
    chk[n] = False
    for i in node[n]:
        if chk[i]:
            virus(i)

N = int(input())
T = int(input())
node = [[] for _ in range(N + 1)]
chk = [True] * (N + 1)
for i in range(T):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)
virus(1)
print(chk.count(False) - 1)