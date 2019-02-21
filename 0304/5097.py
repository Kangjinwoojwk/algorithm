import sys
sys.stdin = open('5097.txt', 'r')
sys.stdout = open('5097_out.txt', 'w')
T = int(input())
for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    li = input().split()
    ans = li[M % N]
    print(f'#{test_case} {ans}')