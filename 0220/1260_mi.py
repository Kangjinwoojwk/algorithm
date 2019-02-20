import sys
sys.stdin = open('1260.txt', 'r')
sys.stdout = open('1260_out.txt', 'w')


def sol(data):
    n = len(data)
    if n == 1:
        return
    for chk in range(1, n):
        if data[chk][0] == data[0][-1]:
            data[0] = data[0] + data[chk]
            data[:] = data[:chk]+data[chk + 1:]
            sol(data)
            break
        if data[chk][-1] == data[0][0]:
            data[chk] = data[chk] + data[0]
            data[:] = data[1:]
            sol(data)
            break


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    get_data = [list(map(int, input().split())) for _ in range(N)]
    hang = []
    x = y = 0
    i = 0
    while i < N:
        j = 0
        while j < N:
            if get_data[i][j] != 0:
                x = y = 1
                while i + x < N and get_data[i + x][j] != 0:
                    x += 1
                while j + y < N and get_data[i][j + y] != 0:
                    y += 1
                for k in range(i, i + x):
                    for l in range(j, j + y):
                        get_data[k][l] = 0
                hang.append([x, y])
            j += 1
        i += 1
    sol(hang)
    hang = hang[0]
    n = len(hang) >> 1
    DP = [[0] * n for _ in range(n)]

