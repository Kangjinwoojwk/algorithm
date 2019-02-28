def BFS(a):
    visited[a] = True
    for i in edge[a]:
        if visited[i] == False:
            visited[i] = True
            q.append(i)


visited = [False] * 8
S = 1
edge = [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [3, 6]]
q = []
q.append(S)
for _ in range(7):
    BFS(q[0])
    print(q[0])
    q = q[1:]
