for _ in range(3):
    sh, sm, ss, eh, em, es = map(int, input().split())
    s, e = sh * 3600 + sm * 60 + ss, eh * 3600 + em * 60 + es
    s = e - s
    h = s // 3600
    s %= 3600
    m = s // 60
    s %= 60
    print(h, m, s)