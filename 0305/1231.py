import sys
sys.stdin = open('1231.txt', 'r')
D, L, R = 0, 1, 2
for test_case in range(1, 11):
    N = int(input())
    tree = [[None, None, None] for _ in range(N + 1)]
    for _ in range(N):
        li = input().split()
        Node, data= int(li[0]), li[1]
        left, right = None, None
        if len(li) == 3:
            left = int(li[2])
        elif len(li) == 4:
            left, right = int(li[2]), int(li[3])
        tree[Node][D], tree[Node][L], tree[Node][R] = data, left, right
    def in_order(v):
        if v == None:
            return
        in_order(tree[v][L])
        print(tree[v][D], end='')
        in_order(tree[v][R])
    print('#{} '.format(test_case), end='')
    in_order(1)
    print()