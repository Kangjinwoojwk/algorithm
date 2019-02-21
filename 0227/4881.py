import sys
sys.stdin = open('4881.txt', 'r')
sys.stdout = open('4881_out.txt', 'w')
T = int(input())


def sol(x, map_arr, garo, Min, N, Sum):
    if len(Min) and Sum > min(Min):
        return
    if x == N:
        Min.append(Sum)
        return
    for i in range(N):
        if garo[i]:
            pass
        else:
            garo[i] = True
            sol(x + 1, map_arr, garo, Min, N, Sum + map_arr[x][i])
            garo[i] = False


for test_case in range(1, T + 1):
    N = int(input())
    map_arr = [list(map(int, input().split())) for _ in range(N)]
    Min = []
    garo = [False] * N
    sol(0, map_arr, garo, Min, N, 0)
    ans = Min[0]
    for i in Min:
        if i < ans:
            ans = i
    print(f'#{test_case} {ans}')

