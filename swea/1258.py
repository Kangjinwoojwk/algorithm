import sys
sys.stdin = open('1258.txt', 'r')
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    result = []
    for i in range(N):
        for j in range(N):
            if data[i][j] != 0:
                row = col = 0
                for k in range(N):
                    if i + k == N or data[i + k][j] == 0:
                        col = k
                        break
                for k in range(N):
                    if j + k == N or data[i][j + k] == 0:
                        row = k
                        break
                for k in range(row):
                    for l in range(col):
                        data[i + l][j + k] = 0
                result.append([row * col, col, row])
    result.sort()
    n = len(result)
    print('#{}'.format(tc), end=' ')
    print(n, end=' ')
    for i in range(n):
        print(result[i][1], result[i][2], end=' ')
    print()
