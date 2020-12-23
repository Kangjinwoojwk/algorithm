import sys
sys.stdin = open('1232.txt', 'r')
sys.stdout = open('1232_out.txt', 'w')
def calculator(v):
    if tree[v][LEFT] == tree[v][RIGHT] == None:
        return tree[v][DATA]
    a = calculator(tree[v][LEFT])
    b = calculator(tree[v][RIGHT])
    if tree[v][DATA] == '+':
        return a + b
    if tree[v][DATA] == '*':
        return a * b
    if tree[v][DATA] == '/':
        return a / b
    if tree[v][DATA] == '-':
        return a - b

DATA, LEFT, RIGHT = 0, 1, 2
for test_case in range(1, 11):
    N = int(input())
    tree = [[None, None, None] for _ in range(N + 1)]
    cal = {'+', '-', '*', '/'}
    for _ in range(N):
        li = input().split()
        li[0] = int(li[0])
        if li[1] in cal:
            tree[li[0]][DATA] = li[1]
            tree[li[0]][LEFT] = int(li[2])
            tree[li[0]][RIGHT] = int(li[3])
        else:
            tree[li[0]][DATA] = int(li[1])
    print('#{} {}'.format(test_case, int(calculator(1))))