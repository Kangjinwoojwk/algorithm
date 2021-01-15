def palindrom(n):
    n = str(n)
    for i in range(len(n) // 2):
        if n[i] != n[- 1 - i]:
            return False
    return True
chk = [False for i in range(1001)]
for i in range(1001):
    if palindrom(i) and (i ** 0.5) % 1 == 0.0 and palindrom(int(i ** 0.5)):
        chk[i] = True
for tc in range(1, int(input()) + 1):
    start, end = map(int, input().split())
    print('#{} {}'.format(tc, chk[start: end + 1].count(True)))