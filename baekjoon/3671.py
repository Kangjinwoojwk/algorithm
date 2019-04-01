ceh = [True] * 10000000
i = 2
ceh[0] = ceh[1] = False
while i < 5000000:
    if ceh[i] == False:
        i += 1
        continue
    j = 2 * i
    while j < 10000000:
        ceh[j] = False
        j += i
    i += 1
def sol(n, it):
    global ans
    i = int(it)
    if ceh[i]:
        result.add(i)
    if n == N:
        return
    for j in range(N):
        if visit[j]:
            visit[j] = False
            sol(n + 1, it + get[j])
            visit[j] = True
    sol(n + 1, it)
ans = []
for _ in range(int(input())):
    get = input()
    N = len(get)
    visit = [True] * N
    result = set()
    sol(0, '0')
    ans.append(str(len(result)))
print('\n'.join(ans))