for _ in range(int(input())):
    A, B = map(int, input().split())
    a, b = A, B
    if a > b:
        a, b = b, a
    while a:
        b -= (b//a) * a
        a, b = b, a
    a = A // b
    print(a * B)
