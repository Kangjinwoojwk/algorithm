import sys
sys.stdin = open('6109.txt', 'r')
def up():
    global N
    for i in range(N):
        for j in range(N):
            if data[i][j] != 0:
                for k in range(i + 1, N):
                    if data[k][j] == data[i][j]:
                        data[k][j] = 0
                        data[i][j] = data[i][j] << 1
                        break
                    elif data[k][j] == 0:
                        continue
                    else:
                        break
    for i in range(N):
        for j in range(N):
            if data[i][j] == 0:
                for k in range(i + 1, N):
                    if data[k][j] != 0:
                        data[k][j], data[i][j] = data[i][j], data[k][j]
                        break
def down():
    global N
    for i in range(N -1, -1, -1):
        for j in range(N):
            if data[i][j] != 0:
                for k in range(i - 1, -1, -1):
                    if data[k][j] == data[i][j]:
                        data[k][j] = 0
                        data[i][j] = data[i][j] <<1
                        break
                    elif data[k][j] == 0:
                        continue
                    else:
                        break
    for i in range(N -1, -1, -1):
        for j in range(N):
            if data[i][j] == 0:
                for k in range(i - 1, -1, -1):
                    if data[k][j] != 0:
                        data[k][j], data[i][j] = data[i][j], data[k][j]
                        break
def left():
    global N
    for i in range(N):
        for j in range(N):
            if data[j][i] != 0:
                for k in range(i + 1, N):
                    if data[j][k] == data[j][i]:
                        data[j][k] = 0
                        data[j][i] = data[j][i] << 1
                        break
                    elif data[j][k] == 0:
                        continue
                    else:
                        break
    for i in range(N):
        for j in range(N):
            if data[j][i] == 0:
                for k in range(i + 1, N):
                    if data[j][k] != 0:
                        data[j][k], data[j][i] = data[j][i], data[j][k]
                        break
def right():
    global N
    for i in range(N - 1, -1, -1):
        for j in range(N):
            if data[j][i] != 0:
                for k in range(i - 1, -1, -1):
                    if data[j][k] == data[j][i]:
                        data[j][k] = 0
                        data[j][i] = data[j][i] << 1
                        break
                    elif data[j][k] == 0:
                        continue
                    else:
                        break
    for i in range(N - 1, -1, -1):
        for j in range(N):
            if data[j][i] == 0:
                for k in range(i - 1, -1, -1):
                    if data[j][k] != 0:
                        data[j][k], data[j][i] = data[j][i], data[j][k]
                        break
T = int(input())
for tc in range(1, T + 1):
    N, direction = input().split()
    N = int(N)
    data = [list(map(int, input().split())) for _ in range(N)]
    if direction == 'up':
        up()
    if direction == 'down':
        down()
    if direction == 'left':
        left()
    if direction == 'right':
        right()
    print('#{}'.format(tc))
    for i in range(N):
        print(' '.join(map(str, data[i])))