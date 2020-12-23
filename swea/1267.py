import sys
sys.stdin = open('1267.txt', 'r')
sys.stdout = open('1267_out.txt', 'w')


def chk(n):
    for i in back_edge[n]:
        if work[i]:
            pass
        else:
            return False
    return True


def sol(n):
    if chk(n):
        work[n] = True
        order.append(n)
        for i in edge[n]:
            if work[i] == False:
                sol(i)


for test_case in range(1, 11):
    V, E = list(map(int, input().split()))
    input_list = list(map(int, input().split()))
    edge = [[] for _ in range(V + 1)]
    back_edge = [[] for _ in range(V + 1)]
    work = [False] * (V + 1)
    order = []
    work[0] = True
    for i in range(E):
        edge[input_list[2 * i]].append(input_list[2 * i + 1])
        back_edge[input_list[2 * i + 1]].append(input_list[2 * i])
    for i in range(1, V + 1):
        if chk(i) and work[i] == False:
            sol(i)
    print('#{}'.format(test_case), end='')
    for i in order:
        print(' {}'.format(i), end='')
    print()
