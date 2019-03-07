import sys
sys.stdin = open('2001.txt', 'r')
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    kill_map = [list(map(int, input().split())) for _ in range(N)]
    def sol(N, M):
        max_value = 0
        for i in range(N - M + 1):
            for j in range(N - M + 1):
                sum = 0
                for k in range(M):
                    for l in range(M):
                        sum += kill_map[i + k][j + l]
                if sum > max_value:
                    max_value = sum
        return max_value
    print('#{} {}'.format(test_case, sol(N, M)))