import time
def cal():
    global ans
    score = 0
    j = 0
    for i in range(N):
        out = 0
        runner = list()
        s = 0
        while out < 3:
            if data[i][line[j]] == 0:
                out += 1
            else:
                runner.append(data[i][line[j]])
            j = (j + 1) % 9
        for k in [-1, -2, -3, -4]:
            s += runner[k]
            if s >= 4:
                if k == - 1:
                    score += len(runner)
                else:
                    score += len(runner[:k + 1])
                break
    if score > ans:
        ans = score


def lin(n):
    if n == 9:
        cal()
        return
    if n == 3:
        lin(4)
    else:
        for i in [1, 2, 3, 4, 5, 6, 7, 8]:
            if visited[i]:
                visited[i] = False
                line[n] = i
                lin(n + 1)
                visited[i] = True


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
t = time.time()
visited = [True] * 9
line = [0] * 9
ans = 0
visited[0] = False
line[3] = 0
lin(0)
print(time.time() - t)
print(ans)