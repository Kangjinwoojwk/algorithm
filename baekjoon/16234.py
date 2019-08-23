dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
N, L, R = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
ans = 0
keep = False
while True:
    visit = [[True] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            union = list()
            union_sum = 0
            st = list()
            if visit[i][j]:
                st.append((i, j))
                union.append((i, j))
                visit[i][j] = False
                union_sum += data[i][j]
                while st:
                    i1, j1 = st.pop()
                    for k in range(4):
                        x, y = i1 + dx[k], j1 + dy[k]
                        if 0 <= x < N and 0 <= y < N and visit[x][y] and L <= abs(data[i1][j1] - data[x][y]) <= R:
                            visit[x][y] = False
                            st.append((x, y))
                            union.append((x, y))
                            union_sum += data[x][y]
                            keep = True
                union_sum //= len(union)
                for k in union:
                    data[k[0]][k[1]] = union_sum
    if keep:
        ans += 1
        keep = False
        continue
    else:
        break
print(ans)