while True:
    data = input()
    if data == 'END':
        break
    else:
        data = ''.join(reversed(list(data)))
        print(data)