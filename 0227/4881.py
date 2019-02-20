import sys
sys.stdin = open('4881.txt', 'r')
sys.stdout = open('4881_out.txt', 'w')
T = int(input())
def sol(map_arr, sero, garo, Min, cnt, N, Sum):
    pass



for test_case in range(1, T + 1):
    N = int(input())
    map_arr = [list(map(int, input().split())) for _ in range(N)]
    Min = []
    sero = [False] * N
    garo = [False] * N
    sol(map_arr, sero, garo, Min, 0, N, 0)

