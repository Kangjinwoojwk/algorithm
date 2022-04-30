dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [1, 1, -1, -1]
dy = [1, -1, 1, -1]
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cloud = [[False] * N for _ in range(N)]
cloud_chk = [[False] * N for _ in range(N)]
cloud[N - 1][0] = cloud[N - 1][1] = cloud[N - 2][0] = cloud[N - 2][1] = True
answer = 0

def create_cloud():
    for i in range(N):
        for j in range(N):
            if board[i][j] >= 2 and not cloud_chk[i][j]:
                board[i][j] -= 2
                cloud[i][j] = True


def cloud_move(d1, d2):
    temp_cloud = [[False] * N for _ in range(N)]
    global cloud_chk, cloud
    for i in range(N):
        for j in range(N):
            if cloud[i][j]:
                temp_cloud[(i + dr[d1] * d2) % N][(j + dc[d1] * d2) % N] = True
    cloud = temp_cloud


def rain():
    global cloud_chk, cloud
    cloud_chk = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if cloud[i][j]:
                cloud[i][j] = False
                cloud_chk[i][j] = True
                board[i][j] += 1


def increase_water():
    for i in range(N):
        for j in range(N):
            if cloud_chk[i][j]:
                for k in range(4):
                    if 0 <= i + dx[k] < N and 0 <= j + dy[k] < N and board[i + dx[k]][j + dy[k]]:
                        board[i][j] += 1


for _ in range(M):
    direction, distance = map(int, input().split())
    cloud_move(direction - 1, distance)
    rain()
    increase_water()
    create_cloud()
for i in board:
    answer += sum(i)
print(answer)
