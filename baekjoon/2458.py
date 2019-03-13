# python3에서 시간이 터지고 pypy3로 맞았다
def big(n):
    for i in li_big[n]:
        if visit[i]:
            visit[i] = False
            big(i)


def small(n):
    for i in li_small[n]:
        if visit[i]:
            visit[i] = False
            small(i)


N, M = map(int, input().split())
li_big = [[] for _ in range(N + 1)]
li_small = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    li_big[a].append(b)
    li_small[b].append(a)
ans = 0
for i in range(1, N + 1):
    visit = [True] * (N + 1)
    visit[0] = False
    visit[i] = False
    big(i)
    small(i)
    if visit.count(False) == N + 1:
        ans += 1
print(ans)