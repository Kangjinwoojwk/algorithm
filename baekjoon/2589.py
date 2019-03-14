dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    global H, W, max_step
    i = 0
    queue = [[x, y]]
    step_map[x][y] = False
    queue_start = 0
    queue_end = 1
    while queue_end - queue_start:
        for j in range(queue_start, queue_end):
            for k in range(4):
                nx, ny = queue[j][0] + dx[k], queue[j][1] + dy[k]
                if 0 <= nx < H and 0 <= ny < W:
                    if step_map[nx][ny] and data[nx][ny] == 'L':
                        step_map[nx][ny] = False
                        queue.append([nx, ny])
        queue = queue[queue_end:]
        queue_end = len(queue)
        if queue_end == 0:
            if i > max_step:
                max_step = i
            return
        i += 1

H, W = map(int, input().split())
data = [input() for _ in range(H)]
max_step = 0
for i in range(H):
    for j in range(W):
        if data[i][j] == 'L':
            step_map = [[True] * W for _ in range(H)]
            bfs(i, j)
print(max_step)