import sys
sys.stdin = open('5356.txt', 'r')
T = int(input())
for tc in range(1, T + 1):
    got = [input() for _ in range(5)]
    print('#{} '.format(tc) + ''.join([got[i][j] for j in range(15) for i in range(5) if j < len(got[i])]))