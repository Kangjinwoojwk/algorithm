import sys
sys.stdin = open('5122.txt', 'r')
sys.stdout = open('5122_input.txt', 'w')
T = int(input())
for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())
    num_list = list(map(int, input().split()))
    for _ in range(M):
        order = input().split()
        if order[0] == 'D':
            idx = int(order[1])
            order = order[0]
        else:
            idx = int(order[1])
            num = int(order[2])
            order = order[0]
        if order == 'I':
            num_list = num_list[:idx] + [num] + num_list[idx:]
        elif order == 'D':
            num_list = num_list[:idx] + num_list[idx + 1:]
        elif order == 'C':
            num_list[idx] = num
    if len(num_list) < L - 1:
        print('#{} -1'.format(test_case))
    else:
        print('#{} {}'.format(test_case, num_list[L]))

