from collections import deque
import sys
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
M, N, H = map(int, input().split())
queue = deque()
data = [[list(map(int, sys.stdin.readline().split()))for __ in range(N)]for ___ in range(H)]
ans = -1
for i in range(H):
    for j in range(N):
        for k in range(M):
            if data[i][j][k] == 1:
                queue.append((i, j, k))
while queue:
    ans += 1
    for _ in range(len(queue)):
        h, n, m = queue.popleft()
        for i in range(6):
            nh, nn, nm = h + dz[i], n + dy[i], m + dx[i]
            if nh < 0 or nh >= H or nn < 0 or nn >= N or nm < 0 or nm >= M:
                continue
            if data[nh][nn][nm] == 0:
                data[nh][nn][nm] = 1
                queue.append((nh, nn, nm))
for i in range(H):
    for j in range(N):
        for k in range(M):
            if data[i][j][k] == 0:
                ans = -1
print(ans)