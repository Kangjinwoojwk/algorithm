import time
def cal():
    global ans
    score = 0
    j = 0
    for i in data:
        out = 0
        s = 0
        while out < 3:
            if i[line[j]] == 0:
                out += 1
            else:
                s = (s << i[line[j]]) + (1 << i[line[j]])
            j = (j + 1) % 9
        score += bin(s >> 4).count('1')
    if score > ans:
        ans = score

def lin(n):
    if n == 0:
        cal()
        return
    if n == 4:
        lin(n - 1)
    else:
        for k in range(n):
            if k == 3:
                continue
            line[k], line[n - 1] = line[n - 1], line[k]
            lin(n - 1)
            line[n - 1], line[k] = line[k], line[n - 1]

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
t = time.time()
line = [1, 2, 3, 0, 4, 5, 6, 7, 8]
ans = 0
lin(9)
print(time.time() - t)
print(ans)