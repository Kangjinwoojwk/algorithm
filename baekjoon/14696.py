N = int(input())
for _ in range(N):
    a = [0, 0, 0, 0]
    b = [0, 0, 0, 0]
    A = list(map(int, input().split()))[1:]
    B = list(map(int, input().split()))[1:]
    for i in A:
        a[4-i] += 1
    for i in B:
        b[4-i] += 1
    if a == b:
        print('D')
    elif a>b:
        print('A')
    else:
        print('B')