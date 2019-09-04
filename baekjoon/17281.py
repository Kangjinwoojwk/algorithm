def cal():
    global ans
    score = 0
    j = 0
    for i in data:
        out = 0
        runner = list()
        while out < 3:
            if i[line[j]] == 0:
                out += 1
            elif i[line[j]] == 4:
                score += len(runner) + 1
                runner = list()
            else:
                for k in range(len(runner) - 1, -1, -1):
                    runner[k] += i[line[j]]
                    if runner[k] >= 4:
                        runner.pop()
                        score += 1
                else:
                    runner.insert(0, i[line[j]])
            j = (j + 1) % 9
    if score > ans:
        ans = score


def lin(n):
    if n == 9:
        cal()
        return
    if n == 3:
        lin(4)
    else:
        for i in range(9):
            if visited[i]:
                visited[i] = False
                line[n] = i
                lin(n + 1)
                visited[i] = True


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

visited = [True] * 9
line = [0] * 9
ans = 0
visited[0] = False
line[3] = 0
lin(0)
print(ans)