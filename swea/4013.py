import sys
sys.stdin = open('4013.txt', 'r')
def sol(n, dir):
    if n < 3 and visit[n + 1]:
        visit[n + 1] = False
        if data[n][2] != data[n + 1][6]:
            sol(n + 1, - dir)
    if n > 0 and visit[n - 1]:
        visit[n - 1] = False
        if data[n][6] != data[n - 1][2]:
            sol(n - 1, -dir)
    if dir == 1:
        data[n] = data[n][7:] + data[n][:7]
    else:
        data[n] = data[n][1:] + data[n][:1]

T = int(input())
for tc in range(1, T + 1):
    K = int(input())
    data = [list(map(int, input().split())) for _ in range(4)]
    for _ in range(K):
        visit = [True] * 4
        a, b = map(int, input().split())
        a -= 1
        visit[a] = False
        sol(a, b)
    ans = data[0][0] + 2 * data[1][0] + 4 * data[2][0] + 8 * data[3][0]
    print('#{} {}'.format(tc, ans))