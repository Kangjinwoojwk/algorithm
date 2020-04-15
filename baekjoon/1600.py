knight = [      (-2, -1),        (-2, 1),
            (-1, -2),                   (-1, 2),

            (1, -2),                    (1, 2),
                (2, -1),         (2, 1)]
monkey = [  (-1, 0),
        (0, -1),    (0, 1),
            (1, 0)]

K = int(input())
W, H = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(H)]
visit = [[[0]*W for _ in range(H)] for __ in range(K + 1)]
visit[K][0][0] = 1
queue = [(K, 0, 0)]
answer = -1
while queue:
    for _ in range(len(queue)):
        jump, x, y = queue.pop(0)
        if jump:
            for i, ii in knight:
                if 0 <= x + i < W and 0 <= y + ii < H and not pan[y + ii][x + i] and not visit[jump - 1][y + ii][x + i]:
                    visit[jump - 1][y + ii][x + i] = visit[jump][y][x] + 1
                    queue.append((jump - 1, x + i, y + ii))
        for i, ii in monkey:
            if 0 <= x + i < W and 0 <= y + ii < H and not pan[y + ii][x + i] and not visit[jump][y + ii][x + i]:
                visit[jump][y + ii][x + i] = visit[jump][y][x] + 1
                queue.append((jump, x + i, y + ii))
    for i in range(K + 1):
        if visit[i][H - 1][W - 1]:
            answer = visit[i][H - 1][W - 1] - 1
    if answer != -1:
        break
print(answer)