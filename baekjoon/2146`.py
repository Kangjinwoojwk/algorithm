# 나중에 더 빠르게 돌아가는 코드를 만들어 보자
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def getmap(x, y, n):
    global N
    get_map[x][y] = n
    st = [(x,y)]
    while st:
        for i in range(len(st)):
            x, y = st.pop()
            for j in range(4):
                nx, ny = x + dx[j], y + dy[j]
                if 0 <= nx < N and 0 <= ny < N and input_map[nx][ny] == 1 and get_map[nx][ny] == 0:
                    get_map[nx][ny] = n
                    st.append((nx, ny))

N = int(input())
input_map = [list(map(int, input().split())) for _ in range(N)]
get_map = [[0] * N for _ in range(N)]
island = 1
for i in range(N):
    for j in range(N):
        if get_map[i][j] == 0 and input_map[i][j] == 1:
            getmap(i, j, island)
            island += 1
input_map = [get_map[i][:] for i in range(N)]
it = True
ans = 0
odd = 0
chk = 0
while it:
    for i in range(N):
        for j in range(N):
            if get_map[i][j] == 0:
                for k in range(4):
                    if 0 <= i + dx[k] < N and 0 <= j + dy[k] < N and get_map[i + dx[k]][j + dy[k]]:
                        if input_map[i][j] != 0 and input_map[i][j] != get_map[i + dx[k]][j + dy[k]]:
                            odd = 1
                            it = False
                        input_map[i][j] = get_map[i + dx[k]][j + dy[k]]
    ans += 2
    for i in range(N):
        for j in range(N):
            if input_map[i][j]:
                for k in range(4):
                    if 0 <= i + dx[k] < N and 0 <= j + dy[k] < N and input_map[i + dx[k]][j + dy[k]]:
                        if input_map[i + dx[k]][j + dy[k]] != input_map[i][j]:
                            it = False
    input_map, get_map = get_map, input_map
print(ans - odd)
