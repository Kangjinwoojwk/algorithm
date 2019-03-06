import sys
sys.stdin = open('5174.txt', 'r')
sys.stdout = open('5174_out.txt', 'w')


def sol(node):
    global cnt
    cnt += 1
    for i in son_node[node]:
        sol(i)


T = int(input())
for test_case in range(1, T + 1):
    E, N = list(map(int, input().split()))
    input_list = list(map(int, input().split()))
    son_node = [[] for _ in range(E + 2)]
    for i in range(E):
        son_node[input_list[2 * i]].append(input_list[2 * i + 1])
    cnt = 0
    sol(N)
    print('#{} {}'.format(test_case, cnt))
