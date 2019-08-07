for tc in range(int(input())):
    max_beer = 0
    ans = ''
    for i in range(int(input())):
        a, b = input().split()
        b = int(b)
        if b > max_beer:
            max_beer = b
            ans = a
    print(ans)