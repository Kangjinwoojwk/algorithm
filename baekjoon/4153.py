while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    A, B, C = abs(a**2 - b**2), (a**2 + b**2), c ** 2
    if A == C or B == C:
        print('right')
    else:
        print('wrong')
