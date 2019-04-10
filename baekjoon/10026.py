dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]
N = int(input())
data = [input() for _ in range(N)]
color = ['G', 'R']
normal = 0
other = 0
visit = [[True] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visit[i][j]:
            visit[i][j] = False
            st = list()
            st.append((i, j))
            normal += 1
            while st:
                x, y = st.pop()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if data[i][j] == data[nx][ny]:
                            if visit[nx][ny]:
                                visit[nx][ny] = False
                                st.append((nx, ny))
visit = [[True] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visit[i][j]:
            visit[i][j] = False
            st = list()
            st.append((i, j))
            other += 1
            while st:
                x, y = st.pop()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if (data[i][j] in color and data[nx][ny] in color) or data[i][j] == data[nx][ny]:
                            if visit[nx][ny]:
                                visit[nx][ny] = False
                                st.append((nx, ny))
print(normal, other)
