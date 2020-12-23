for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    root = [i for i in range(V + 1)]
    edge = [list(map(int, input().split()))for _ in range(E)]
    edge.sort(key = lambda st:st[2])
    ans = 0
    cnt = 0
    for i in edge:
        if root[i[0]] != root[i[1]]:
            chk = root[i[0]]
            for j in range(V + 1):
                if root[j] == chk:
                    root[j] = root[i[1]]
            ans += i[2]
            cnt += 1
        if cnt == V:
            break
    print('#{} {}'.format(tc, ans))