dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
N, M = map(int, input().split())
data = [list(input()) for _ in range(M)]
cord = [[0, 0]] * 7
cnt = 1
ans = 1000000
for i in range(M):
    for j in range(N):
        if data[i][j] == 'S':
            cord[0] = [i, j]
        elif data[i][j] == 'X':
            cord[cnt] = [i, j]
            data[i][j] = cnt
            cnt += 1
        elif data[i][j] == 'E':
            cord[6] = [i, j]
cord[cnt] = cord[6]
data[cord[0][0]][cord[0][1]] = 0
data[cord[cnt][0]][cord[cnt][1]] = cnt
distance = [[10000] * (cnt + 1) for _ in range(cnt + 1)]
for i in range(cnt + 1):
    visit = [[10000] * N for _ in range(M)]
    visit[cord[i][0]][cord[i][1]] = 0
    distance[i][i] = 0
    queue = [(cord[i][0], cord[i][1])]
    while 10000 in distance[i]:
        for j in range(len(queue)):
            x, y = queue.pop(0)
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if data[nx][ny] != '#' and visit[nx][ny] == 10000:
                    visit[nx][ny] = visit[x][y] + 1
                    queue.append((nx, ny))
                    if [nx, ny] in cord:
                        distance[data[nx][ny]][i] = distance[i][data[nx][ny]] = visit[x][y] + 1

order = [0] * (cnt + 1)
order[cnt] = cnt
visit = [True] * (cnt + 1)
visit[0] = visit[-1] = False
def cal():
    global ans
    dist = 0
    for l in range(cnt):
        dist += distance[order[l]][order[l + 1]]
    if dist < ans:
        ans = dist


def sol(n):
    if n == cnt:
        cal()
        return
    for m in range(1, cnt):
        if visit[m]:
            visit[m] = False
            order[n] = m
            sol(n + 1)
            visit[m] = True


sol(1)
print(ans)