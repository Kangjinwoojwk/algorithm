while True:
    try:
        a, b = '0', '1'
        n = int(input())
        p = input()
        for i in range(n):
            a, b = b, b + a

    except EOFError:
        break