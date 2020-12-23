T = int(input())
for tc in range(1, T + 1):
    bi = input()
    tri = input()
    b = set()
    t = set()
    for i in range(len(bi)):
        a = 0
        for j in range(len(bi)):
            if i == j:
                a = a * 2 + ((int(bi[j]) + 1) % 2)
            else:
                a = a * 2 + int(bi[j])
        b.add(a)
    for i in range(len(tri)):
        a = 0
        c = 0
        for j in range(len(tri)):
            if i == j:
                a = a * 3 + ((int(tri[j]) + 1) % 3)
                c = c * 3 + ((int(tri[j]) + 2) % 3)
            else:
                a = a * 3 + int(tri[j])
                c = c * 3 + int(tri[j])
        t.add(a)
        t.add(c)
    for i in t:
        if i in b:
            ans = i
    print('#{} {}'.format(tc, ans))