import sys
sys.stdin = open('4014.txt', 'r')
def sol(n):
    global N, X, ans

T = int(input())
for tc in range(1, T + 1):
    N, X = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        sol(i)
    print('#{} {}'.format(tc, ans))
