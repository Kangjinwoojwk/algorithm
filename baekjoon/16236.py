dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
N = int(input())
answer = 0
space = [list(map(int, input().split())) for _ in range(N)]
baby_shark_loc = [0, 0]
for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            baby_shark_loc = [i, j]
            space[i][j] = 0
eat_fish = 0
baby_shark_size = 2
queue = [[baby_shark_loc], []]
t = 0
visited = [[False] * N for _ in range(N)]
visited[baby_shark_loc[0]][baby_shark_loc[1]] = True
while True:
    if not queue[0]:
        break
    for _ in range(len(queue[0])):
        tempx, tempy = queue[0].pop(0)
        if 0 < space[tempx][tempy] < baby_shark_size:
            space[tempx][tempy] = 0
            eat_fish += 1
            answer += t
            baby_shark_loc = [tempx, tempy]
            if eat_fish == baby_shark_size:
                baby_shark_size += 1
                eat_fish = 0
            queue = [[baby_shark_loc], []]
            visited = [[False] * N for _ in range(N)]
            visited[baby_shark_loc[0]][baby_shark_loc[1]] = True
            t = 0
            break
        else:
            for i in range(4):
                if 0 <= tempx + dx[i] < N and 0 <= tempy + dy[i] < N and not visited[tempx + dx[i]][tempy + dy[i]] and \
                        space[tempx + dx[i]][tempy + dy[i]] <= baby_shark_size:
                    for j in range(len(queue[1])):
                        if [tempx + dx[i], tempy + dy[i]] < queue[1][j]:
                            queue[1].insert(j, [tempx + dx[i], tempy + dy[i]])
                    else:
                        queue[1].append([tempx + dx[i], tempy + dy[i]])
                    visited[tempx + dx[i]][tempy + dy[i]] = True
    else:
        t += 1
        queue.pop(0)
        queue.append(list())
print(answer)