A, B = 100, 100
for tc in range(int(input())):
    a, b = map(int, input().split())
    if a > b:
        B -= a
    elif b > a:
        A -= b
print('{}\n{}'.format(A, B))