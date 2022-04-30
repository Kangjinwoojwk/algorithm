dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
board_temp = [[0] * N for _ in range(N)]
location = list()
point = [N//2, N//2]
answer = 0
for i in range(2, N, 2):
    for j in range(4):
        for k in range(i):
            if j == 0 and k == 0:
                point[1] -= 1
            else:
                point[0] += dr[j]
                point[1] += dc[j]
            location.append(point[:])


def destroy(d1, d2):
    for i in range(d2 + 1):
        board[N//2 + dx[d1] * i][N//2 + dy[d1] * i] = 0


def explosion():
    global answer
    count = 0
    temp = [board[location[i][0]][location[i][1]] for i in range(N * N - 1) if board[location[i][0]][location[i][1]]]
    curr = [0, 0]
    n = len(temp)
    for i in range(len(temp)):
        if temp[i] != curr[0]:
            if curr[1] >= 4:
                for j in range(i - 1, i - 1 - curr[1], -1):
                    answer += temp[j]
                    count += 1
                    temp[j] = 0
            curr[0] = temp[i]
            curr[1] = 1
        else:
            curr[1] += 1
    if curr[1] >= 4:
        for j in range(n - 1, n - 1 - curr[1], -1):
            answer += temp[j]
            count += 1
            temp[j] = 0
    n = len(temp)
    for i in range(N * N - 1):
        if i < n:
            board[location[i][0]][location[i][1]] = temp[i]
        else:
            board[location[i][0]][location[i][1]] = 0

    return count


def move():
    temp = [board[location[i][0]][location[i][1]] for i in range(N * N - 1) if board[location[i][0]][location[i][1]]]
    n = len(temp)
    for i in range(N * N -1):
        if i < n:
            board[location[i][0]][location[i][1]] = temp[i]
        else:
            board[location[i][0]][location[i][1]] = 0


def multiply():
    temp = [board[location[i][0]][location[i][1]] for i in range(N * N - 1) if board[location[i][0]][location[i][1]]]
    temp2 = list()
    curr = [0, 0]
    for i in range(len(temp)):
        if temp[i] != curr[0]:
            if curr[0]:
                temp2.append(curr[1])
                temp2.append(curr[0])
            curr[0] = temp[i]
            curr[1] = 1
        else:
            curr[1] += 1
    temp2.append(curr[1])
    temp2.append(curr[0])
    n = len(temp2)
    for i in range(N * N - 1):
        if i < n:
            board[location[i][0]][location[i][1]] = temp2[i]
        else:
            board[location[i][0]][location[i][1]] = 0

for _ in range(M):
    direction, distance = map(int, input().split())
    destroy(direction - 1, distance)
    move()
    n = explosion()
    while n:
        move()
        n = explosion()
    multiply()
print(answer)