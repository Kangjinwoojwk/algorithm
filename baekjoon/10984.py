for tc in range(int(input())):
    A, G = 0, 0
    for i in range(int(input())):
        a, b = map(float, input().split())
        A += a
        G += a * b
    G /= A
    print('{} {}'.format(int(A), round(G, 1)))