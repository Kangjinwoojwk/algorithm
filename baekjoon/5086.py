while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    if b % a :
        if a % b :
            print('neither')
        else:
            print('multiple')
    else:
        print('factor')