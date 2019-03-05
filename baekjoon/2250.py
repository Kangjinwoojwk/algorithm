def sol(v, level, width):
    if v == -1:
        return width
    global Max_level
    if Max_level < level:
        Max_level = level
    location[v][0] = level
    location[v][1] = 1 + sol(L[v], level + 1, width)
    return sol(R[v], level + 1, location[v][1])

N = int(input())
L = [0] * (N + 1)
R = [0] * (N + 1)
Max_level = 0
location = [[0, 0] for i in range(N + 1)]
exist = [True] * (N + 1)
exist[0] = False
start = 0
for _ in range(N):
    node, left, right = map(int, input().split())
    if right != -1:
        exist[right] = False
    if left != -1:
        exist[left] = False
    R[node] = right
    L[node] = left
for i in range(1, N + 1):
    if exist[i]:
        start = i
sol(start, 1, 0)
li = [[] for _ in range(Max_level + 1)]
for i in location:
    li[i[0]].append(i[1])
li = [max(li[i]) - min(li[i]) + 1 for i in range(Max_level + 1)]
max_width = max(li)
for i in range(1, Max_level + 1):
    if max_width == li[i]:
        print(i, max_width)
        break