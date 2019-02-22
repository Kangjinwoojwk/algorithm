import sys
sys.stdin = open('5102.txt', 'r')
sys.stdout = open('5102_out.txt', 'w')
# 도착 못하는 경우 0 출력

def sol(now, goal, step):
    global min_step
    global Node
    global old_node
    if now == goal and step < min_step:
        min_step = step
        return
    if step >= min_step:
        return
    old_node += [now]
    for i in Node:
        if i[0] == now and i[1] not in old_node:
            sol(i[1], goal, step + 1)
        if i[1] == now and i[0] not in old_node:
            sol(i[0], goal, step + 1)
    old_node = old_node[:-1]
    return


T = int(input())
for test_case in range(1, T + 1):
    V, E = list(map(int, input().split()))
    Node = [list(map(int, input().split()))for _ in range(E)]
    S, G = list(map(int, input().split()))
    old_node = []
    min_step = 100000
    sol(S, G, 0)
    if min_step == 100000:
        min_step = 0
    print('#{} {}'.format(test_case, min_step))


