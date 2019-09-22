while True:
    profit, minus, allcnt, bomb = map(int, input().split())
    ans = 0
    while True:
        if ((profit * (allcnt - bomb)) - (minus * bomb))/allcnt > 0:
            ans += 1
            allcnt -= 1
        else:
            break
    print(ans)