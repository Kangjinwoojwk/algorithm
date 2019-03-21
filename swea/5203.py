T = int(input())
for tc in range(1, T + 1):
    li = list(map(int, input().split()))
    player = [[0] * 10 for _ in range(2)]
    for i in range(12):
        p = i % 2
        player[p][li[i]] += 1
        if 3 in player[p]:
            print('#{} {}'.format(tc, (p) + 1))
            break
        else:
            chk = False
            for j in range(8):
                if player[p][j] > 0 and player[p][j + 1] > 0 and player[p][j + 2]> 0:
                    print('#{} {}'.format(tc, (p) + 1))
                    chk = True
                    break
            if chk:
                break
    else:
        print('#{} {}'.format(tc, 0))