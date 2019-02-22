import sys
sys.stdin = open('5110.txt', 'r')
sys.stdout = open('5110_out.txt', 'w')
T = int(input())
for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    data = [list(map(int, input().split())) for _ in range(M)]
    


