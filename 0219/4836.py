import sys
sys.stdin = open('4836.txt', 'r')
sys.stdout = open('4836_out.txt', 'w')
T = int(input())
for test_case in range(1, T + 1):
    color_map = [[0] * 10 for i in range(10)]
    N = int(input())
    for _ in range(N):
        x_left, y_up, x_right, y_down, color = list(map(int, input().split()))
        for i in range(x_left, x_right + 1):
            for j in range(y_up, y_down + 1):
                color_map[i][j] += color
    count = 0
    for i in color_map:
        for j in i:
            if j == 3:
                count += 1

    print(f'#{test_case} {count}')
