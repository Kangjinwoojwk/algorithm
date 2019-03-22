d = [[],
     [[(-1, 0)], [(0, 1)], [(1, 0)], [(0, -1)]],
     [[(-1, 0), (1, 0)],[(0, 1), (0, -1)]],
     [[(-1, 0), (0, 1)],[(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)]],
     [[(0, -1), (-1, 0),(0, 1)], [(-1, 0),(0, 1), (1, 0)], [(0, 1), (1, 0), (0, -1)], [(1, 0), (0, -1), (-1, 0)]],
     [[(-1, 0),(0, 1), (1, 0), (0, -1)]]
     ]
def cal():
    global ans, N, M
    for i in camera:
        for j in d[i[0]][i[3]]:
            for k in range(1, max(N, M)):
                x, y = i[1] + k * j[0], i[2] + k * j[1]
                if x < 0 or x >= N or y < 0 or y >= M:
                    break
                if data[x][y] == '6':
                    break
                if data[x][y] == '0':
                    data[x][y] = '#'
    sagak = 0
    for i in range(N):
        for j in range(M):
            if data[i][j] == '0':
                sagak += 1
            elif data[i][j] == '#':
                data[i][j] = '0'
    if sagak < ans:
        ans = sagak

def sol(n):
    global cnt
    if n == cnt:
        cal()
        return
    for i in range(ca[camera[n][0]]):
        camera[n][3] = i
        sol(n + 1)

N, M = map(int, input().split())
data = [input().split() for _ in range(N)]
ca = [0, 4, 2, 4, 4, 1]
camera = []
cnt = 0
ans = 64
for i in range(N):
    for j in range(M):
        if 49 <= ord(data[i][j]) <= 53:
            camera.append([int(data[i][j]), i, j, 0])
            cnt += 1
sol(0)
print(ans)