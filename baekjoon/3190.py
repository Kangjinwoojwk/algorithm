dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
N = int(input())
data = [[0] * N for _ in range(N)]
data[0][0] = 1
direction = 1
snake = [[0, 0]]
for _ in range(int(input())):
    x, y = map(int, input().split())
    data[x - 1][y - 1] = 2
data2 = [input().split() for _ in range(int(input()))]
for i in data2:
    i[0] = int(i[0])
    i[1] = -1 if i[1] == 'L' else 1
data2.append([0, 0])
ans = 0
data2_ptr = 0
while True:
    if ans == data2[data2_ptr][0]:
        direction = (direction + data2[data2_ptr][1]) % 4
        data2_ptr += 1
    ans += 1
    snake.insert(0, [snake[0][0] + dx[direction], snake[0][1] + dy[direction]])
    if 0 <= snake[0][0] < N and 0 <= snake[0][1] < N:
        if data[snake[0][0]][snake[0][1]] == 1:
            break
        if data[snake[0][0]][snake[0][1]] == 2:
            data[snake[0][0]][snake[0][1]] = 1
        else:
            data[snake[0][0]][snake[0][1]] = 1
            data[snake[-1][0]][snake[-1][1]] = 0
            snake.pop()
    else:
        break
print(ans)