T = int(input())
for tc in range(1, T + 1):
    get = float(input())
    ans = ''
    for i in range(12):
        get *= 2
        ans += str(int(get))
        get %= 1
        if get == 0:
            break
    else:
        print('#{} overflow'.format(tc))
        continue
    print('#{} {}'.format(tc, ans))