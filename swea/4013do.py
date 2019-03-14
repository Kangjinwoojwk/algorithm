import sys
sys.stdin = open('4013.txt', 'r')
def sol(n, dir):
    if dir == 1:
        data[n] = data[n][7:] + data[n][:7]
    else:
        data[n] = data[n][1:] + data[n][:1]

T = int(input())
for tc in range(1, T + 1):
    K = int(input())
    data = [list(map(int, input().split())) for _ in range(4)]
    for _ in range(K):

    print(data[0][0] + 2 * data[1][0] + 4 * data[2][0] + 8 * data[3][0])