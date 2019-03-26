from collections import deque
def dfs(n):
    Dfs.append(n)
    visit[n] = False
    for i in edge[n]:
        if visit[i]:
            dfs(i)

N, M, V = map(int, input().split())
edge = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)
for i in range(N + 1):
    edge[i].sort()
visit = [True] * (N + 1)
st = deque()
st.append(V)
visit[V] = False
Bfs = [V]
while st:
    for _ in range(len(st)):
        a = st.popleft()
        for i in edge[a]:
            if visit[i]:
                visit[i] = False
                Bfs.append(i)
                st.append(i)
visit = [True] * (N + 1)
Dfs = []
dfs(V)
print(' '.join(map(str, Dfs)))
print(' '.join(map(str, Bfs)))
