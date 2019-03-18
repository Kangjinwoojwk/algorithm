T = int(input())
for _ in range(T):
    order = input()
    N = int(input())
    get = input()
    get = get[1:-1]
    get = get.split(',')
    if order.count('D') > N:
        print('error')
        continue
    chk = True
    for i in order:
        if i == 'D':
            if chk:
                del get[0]
            else:
                del get[-1]
        if i == 'R':
            if chk:
                chk = False
            else:
                chk = True
    if chk == False:
        get.reverse()
    print('[', end='')
    print(','.join(get), end='')
    print(']')