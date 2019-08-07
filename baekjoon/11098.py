for tc in range(int(input())):
    max_beer = 0
    ans = ''
    for i in range(int(input())):
        a, b = input().split()
        a = int(a)
        if a > max_beer:
            max_beer = a
            ans = b
    print(ans)