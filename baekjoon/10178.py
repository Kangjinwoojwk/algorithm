for tc in range(int(input())):
    candy, brother = map(int, input().split())
    print('You get {} piece(s) and your dad gets {} piece(s).'.format(candy // brother, candy % brother))