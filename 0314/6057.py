T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    Node = [[] for i in range(N + 1)]
    ans = 0
    for i in range(M):
        x, y = map(int, input().split())
        Node[x].append(y)
        Node[y].append(x)
    for i in range(1, N + 1):
        for j in Node[i]:
            for k in Node[j]:
                if k != i:
                    for l in Node[k]:
                        if i == l:
                            ans += 1
    print('#{} {}'.format(tc, ans // 6))