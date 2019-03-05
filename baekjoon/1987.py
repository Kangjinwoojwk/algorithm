dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def sol(x, y, cnt):
    global ans, R, C
    if cnt > ans:
        ans = cnt
    for i in range(4):
        next_x, next_y = x + dx[i], y + dy[i]
        if next_x < 0 or next_y < 0 or next_x >= R or next_y >= C:
            continue
        if visited[ord(board[next_x][next_y])-ord('A')]:
            continue
        visited[ord(board[next_x][next_y]) - ord('A')] = True
        sol(next_x, next_y, cnt + 1)
        visited[ord(board[next_x][next_y]) - ord('A')] = False

R, C = map(int, input().split())
board = [input() for _ in range(R)]
visited = [False] * 26
ans = 0
visited[ord(board[0][0]) - ord('A')] = True
sol(0, 0, 1)
print(ans)
