import sys
sys.stdin = open('DFS_input.txt', 'r')

def DFS(v):
    S = []
    visit[v] = True
    print(v, end=' ')
    S.append(v)
    while len(S) > 0:
        goback = True
        for w in G[v]:
            if not visit[w]:
                visit[w] = True
                print(w, end=' ')
                S.append(v)
                v = w
                goback = False
                break
        if goback:
            v = S.pop(-1)


V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
visit = [False for _ in range(V + 1)]
for i in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

DFS(1)
