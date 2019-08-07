for tc in range(int(input())):
    Y, K = 0, 0
    for i in range(9):
        y, k = map(int, input().split())
        Y += y
        K += k
    if Y == K:
        print('Draw')
    elif Y > K:
        print('Yonsei')
    else:
        print('Korea')