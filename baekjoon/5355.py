for _ in range(int(input())):
    data = input().split()
    a = float(data.pop(0))
    while data:
        temp = data.pop(0)
        if temp == '@':
            a *=3
        elif temp == '%':
            a += 5
        elif temp == '#':
            a -= 7
    print('%0.2f' % a)