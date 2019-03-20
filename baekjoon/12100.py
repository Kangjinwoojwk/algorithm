def up(n):
    global N
    for i in range(N):
        for j in range(N):
            if data[n][j][i]:
                for k in range(j + 1, N):
                    if data[n][k][i] == 0:
                        continue
                    elif data[n][k][i] != data[n][j][i]:
                        break
                    elif data[n][k][i] == data[n][j][i]:
                        data[n][j][i] *= 2
                        data[n][k][i] = 0
                        break
    for i in range(N):
        for j in range(N):
            if data[n][j][i] == 0:
                for k in range(j + 1, N):
                    if data[n][k][i] != 0:
                        data[n][k][i], data[n][j][i] = data[n][j][i], data[n][k][i]
                        break
                else:
                    break
    sol(n)


def down(n):
    global N
    for i in range(N):
        for j in range(N - 1, -1, -1):
            if data[n][j][i]:
                for k in range(j - 1, -1, -1):
                    if data[n][k][i] == 0:
                        continue
                    elif data[n][k][i] != data[n][j][i]:
                        break
                    elif data[n][k][i] == data[n][j][i]:
                        data[n][j][i] *= 2
                        data[n][k][i] = 0
                        break
    for i in range(N):
        for j in range(N - 1, -1, -1):
            if data[n][j][i] == 0:
                for k in range(j - 1, -1, -1):
                    if data[n][k][i] != 0:
                        data[n][k][i], data[n][j][i] = data[n][j][i], data[n][k][i]
                        break
                else:
                    break
    sol(n)


def left(n):
    global N
    for i in range(N):
        for j in range(N):
            if data[n][i][j]:
                for k in range(j + 1, N):
                    if data[n][i][k] == 0:
                        continue
                    elif data[n][i][k] != data[n][i][j]:
                        break
                    elif data[n][i][k] == data[n][i][j]:
                        data[n][i][j] *= 2
                        data[n][i][k] = 0
                        break
    for i in range(N):
        for j in range(N):
            if data[n][i][j] == 0:
                for k in range(j + 1, N):
                    if data[n][i][k] != 0:
                        data[n][i][k], data[n][i][j] = data[n][i][j], data[n][i][k]
                        break
                else:
                    break
    sol(n)


def right(n):
    global N
    for i in range(N):
        for j in range(N - 1, -1, -1):
            if data[n][i][j]:
                for k in range(j - 1, -1, -1):
                    if data[n][i][k] == 0:
                        continue
                    elif data[n][i][k] != data[n][i][j]:
                        break
                    elif data[n][i][k] == data[n][i][j]:
                        data[n][i][j] *= 2
                        data[n][i][k] = 0
                        break
    for i in range(N):
        for j in range(N - 1, -1, -1):
            if data[n][i][j] == 0:
                for k in range(j - 1, -1, -1):
                    if data[n][i][k] != 0:
                        data[n][i][k], data[n][i][j] = data[n][i][j], data[n][i][k]
                        break
                else:
                    break
    sol(n)


def sol(n):
    global ans, N
    if n == 5:
        for i in range(N):
            for j in range(N):
                if data[5][i][j] > ans:
                    ans = data[5][i][j]
        return
    for i in range(4):
        for j in range(N):
            for k in range(N):
                data[n + 1][j][k] = data[n][j][k]
        if i == 0:
            up(n + 1)
        elif i == 1:
            down(n + 1)
        elif i == 2:
            left(n + 1)
        elif i == 3:
            right(n + 1)


N = int(input())
data = [[list(map(int, input().split())) for _ in range(N)]]
for i in range(5):
    data.append([[0] * N for _ in range(N)])
ans = 0
sol(0)
print(ans)