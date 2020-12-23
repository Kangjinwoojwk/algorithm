import sys
sys.stdin = open('tree_input.txt', 'r')
def inorder(v):
    if v == 0: return
    # 전위
    inorder(L[v])
    # 중위
    print(v, end = ' ')
    inorder(R[v])
    # 후위
# 트리의 높이를 계산하는 함수 작성
def treeHeight(v):
    if v == 0: return 0
    a = 1 + treeHeight(L[v])
    b = 1 + treeHeight(R[v])
    return max(a, b)

# 높이가 3인 노드들을 출력하시오
def node_print(v, cnt, depth):
    if v == 0:return
    if cnt == depth:
        print(v, end=' ')
        return
    node_print(L[v], cnt + 1, depth)
    node_print(R[v], cnt + 1, depth)

# 특정 노드가 루트인 트리의 전체 노드 수
def treeSize(v):
    if v == 0:return 0
    return 1 + treeSize(L[v]) + treeSize(R[v])
# 임의 두 노드의 공통 조상을 찾는 함수
def who_is_parent(v, u):
    global V
    if u == v:
        return u
    a = None
    for i in range(1, V +1):
        if L[i] == v or R[i] == v:
            a = who_is_parent(i, u)
        if L[i] == u or R[i] == u:
            a = who_is_parent(v, i)
    return a
V, E = map(int, input().split())
arr = list(map(int, input().split()))
L = [0] * (V + 1)
R = [0] * (V + 1)
P = [0] * (V + 1)
for i in range(0, E * 2, 2):
    u, v = arr[i], arr[i + 1]
    if L[u] == 0:
        L[u] = v
    else:
        R[u] = v
inorder(1)
print()
print(treeHeight(1))
node_print(1, 0, 3)
print()
print(treeSize(3))
print(who_is_parent(8, 11))






# import sys
# sys.stdin = open('tree_input.txt', 'r')
# V, E = map(int, input().split())
# tree = [[None, None] for _ in range(V + 1)]
# input_list = list(map(int, input().split()))
# for i in range(E):
#     if tree[input_list[2 * i]][0] == None:
#         tree[input_list[2 * i]][0] = input_list[2 * i + 1]
#     else:
#         tree[input_list[2 * i]][1] = input_list[2 * i + 1]
# print(tree)