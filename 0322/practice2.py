T = input()
li = [0] * 10
for i in T:
    li[int(i)] += 1
chk = 0
for i in range(10):
    if li[i] == 6:
        li[i] -= 6
        chk = 2
        break
    elif li[i] >= 3:
        li[i] -= 3
        chk += 1
if chk != 2:
    for i in range(8):
        if li[i] == li[i + 1] == li[i + 2] == 2:
            li[i] = li[i + 1] = li[i + 2] = 0
            chk = 2
        elif li[i] > 0 and li[i + 1] > 0 and li[i + 2] > 0:
            li[i] -= 1
            li[i + 1] -= 1
            li[i + 2] -= 1
            chk += 1
if chk == 2:
    print('Baby-gin!')
else:
    print('not baby-gin')