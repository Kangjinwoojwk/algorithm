def sol(x, y, cnt):
    global ans
    if x == 10:
        if cnt < ans:
            ans = cnt
        return
    if cnt >= ans:
        return
    if data[x][y] == 0:
        if y == 9:
            return sol(x + 1, 0, cnt)
        else:
            return sol(x, y + 1, cnt)
    for i in range(5, 0, -1):
        for j in range(i ** 2):
            if x + (j // i) > 9 or y + (j % i) > 9:
                break
            elif data[x + (j // i)][y + (j % i)] == 0:
                break
        else:
            if it[i]:
                it[i] -= 1
                for j in range(i):
                    for k in range(i):
                        data[x + j][y + k] = 0
                if y == 9:
                    sol(x + 1, 0, cnt + 1)
                else:
                    sol(x, y + 1, cnt + 1)
                for j in range(i):
                    for k in range(i):
                        data[x + j][y + k] = 1
                it[i] += 1


data = [list(map(int, input().split())) for _ in range(10)]
it = [0, 5, 5, 5, 5, 5]
ans = 30
sol(0, 0, 0)
if ans == 30:
    ans = -1
print(ans)