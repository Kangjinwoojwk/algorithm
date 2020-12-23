import sys
sys.stdin = open('1209.txt', 'r')
sys.stdout = open('1209_output', 'w')
for _ in range(10):
    test_case = int(input())
    arr = [[]for __ in range(100)]
    for i in range(100):
        arr[i] = list(map(int, input().split()))
    max_sum = 0
    for i in range(100):
        sum_v = 0
        for j in range(100):
            sum_v += arr[i][j]
        if max_sum < sum_v:
            max_sum = sum_v
    for i in range(100):
        sum_v = 0
        for j in range(100):
            sum_v += arr[j][i]
        if max_sum < sum_v:
            max_sum = sum_v
    sum_v = 0
    for i in range(100):
        sum_v += arr[i][i]
    if max_sum < sum_v:
        max_sum = sum_v
    sum_v = 0
    for i in range(100):
        sum_v += arr[99 - i][i]
    if max_sum < sum_v:
        max_sum = sum_v
    print(f'#{test_case} {max_sum}')
