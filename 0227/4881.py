import sys
sys.stdin = open('4881.txt', 'r')
sys.stdout = open('4881_out.txt', 'w')
T = int(input())


def sol(x, N, Sum):
    global Min
    if Sum > Min:
        return
    if x == N:
        if Min > Sum:
            Min = Sum
        return
    for i in range(N):
        if garo[i]:
            pass
        else:
            garo[i] = True
            sol(x + 1, N, Sum + map_arr[x][i])
            garo[i] = False


for test_case in range(1, T + 1):
    N = int(input())
    map_arr = [list(map(int, input().split())) for _ in range(N)]
    Min = 100000000
    garo = [False] * N
    sol(0, N, 0)
    print('#{} {}'.format(test_case, Min))

