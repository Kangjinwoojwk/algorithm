for tc in range(1, int(input()) + 1):
    p, q = map(int, input().split())
    px, py, qx, qy, pc, qc = 0, 0, 0, 0, 0, 0
    chk = 0
    for i in range(1, 10000):
        if px and qx:
            break
        chk += i
        if not px and p <= chk:
            px = i
            pc = chk
        if not qx and q <= chk:
            qx = i
            qc = chk
    py = 1 + pc - p
    px -= (pc - p)
    qy = 1 + qc - q
    qx -= (qc - q)
    x, y = px + qx, py + qy
    answer = sum(range(x+y )) - (y - 1)
    print('#{} {}'.format(tc, answer))
