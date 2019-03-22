W, B, R = 0, 1, 2
color = ['W', 'B', 'R']
def sol(line, color, cnt):
    global N, ans
    if cnt >= ans:
        return
    if line == N:
        if color != 2:
            return
        ans = cnt
        return
    if line == 0:
        cnt += li[line][B] + li[line][R]
        sol(line + 1, color, cnt)
        sol(line + 1, color + 1, cnt)
    elif line == N - 1:
        cnt += li[line][W] + li[line][B]
        sol(line + 1, color, cnt)
    else:
        if color == 0:
            cnt += li[line][B] + li[line][R]
            sol(line + 1, color, cnt)
            sol(line + 1, color + 1, cnt)
        elif color == 1:
            cnt += li[line][W] + li[line][R]
            sol(line + 1, color, cnt)
            sol(line + 1, color + 1, cnt)
        elif color == 2:
            cnt += li[line][W] + li[line][B]
            sol(line + 1, color, cnt)

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]
    li = [[data[i].count('W'), data[i].count('B'), data[i].count('R')] for i in range(N)]
    ans = 2500
    sol(0, 0, 0)
    print('#{} {}'.format(tc, ans))