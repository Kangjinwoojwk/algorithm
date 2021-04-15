n, k = map(int, input().split())
answer = 0
chk = ['acint', 'bdefghjklmopqrsuvwxyz', [False] * 21]
word = [input()[4:-4] for _ in range(n)]


def count():
    global answer
    c = chk[0]
    cnt = 0
    for j in range(21):
        if chk[2][j]:
            c += chk[1][j]
    for j in word:
        for l in j:
            if l not in c:
                break
        else:
            cnt += 1
    if cnt > answer:
        answer = cnt


def sol(number, s):
    if number == 0:
        count()
        return
    for i in range(s, 21):
        if not chk[2][i]:
            chk[2][i] = True
            sol(number - 1, i + 1)
            chk[2][i] = False
    return


if k >= 5:
    sol(k - 5, 0)
print(answer)