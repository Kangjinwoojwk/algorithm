for _ in range(int(input())):
    get = input()
    value = 0
    for i in range(3):
        value *= 26
        value += ord(get[i]) - ord('A')
    value -= int(get[4:])
    if abs(value) <= 100:
        print('nice')
    else:
        print('not nice')