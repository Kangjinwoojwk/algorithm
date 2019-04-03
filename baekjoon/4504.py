N = int(input())
a = [True if i % N == 0 else False for i in range(10000)]
while True:
    b = int(input())
    if b == 0:
        break
    else:
        if a[b]:
            print('{} is a multiple of {}.'.format(b, N))
        else:
            print('{} is NOT a multiple of {}.'.format(b, N))