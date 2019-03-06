def got(a):
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == a:
                bingo[i][j] = '#'
def chk():
    cnt = 0
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == '#':
                continue
            break
        else:
            cnt += 1
    for i in range(5):
        for j in range(5):
            if bingo[j][i] == '#':
                continue
            break
        else:
            cnt += 1
    for i in range(5):
        if bingo[i][i] == '#':
            continue
        break
    else:
        cnt += 1
    for i in range(5):
        if bingo[i][4 - i] == '#':
            continue
        break
    else:
        cnt += 1
    if cnt >= 3:
        return False
    return True
bingo = [list(map(int, input().split())) for _ in range(5)]
call = list(map(int, input().split()))
for _ in range(4):
    call.extend(list(map(int, input().split())))
i = 0
while chk():
    got(call[i])
    i += 1
print(i)
