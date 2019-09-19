for tc in range(int(input())):
    P, M = map(int, input().split())
    visit = [False] * (M + 1)
    ans = 0
    for _ in range(P):
        a = int(input())
        if visit[a]:
            ans += 1
        else:
            visit[a] = True
    print(ans)
