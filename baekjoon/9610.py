Q = [0, 0, 0, 0, 0]
for tc in range(int(input())):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        Q[4] += 1
    elif x > 0 and y > 0:
        Q[0] += 1
    elif x < 0 < y:
        Q[1] += 1
    elif x < 0 and y < 0:
        Q[2] += 1
    elif x > 0 > y:
        Q[3] += 1
for i in range(5):
    if i != 4:
        print('Q{}: {}'.format(i + 1, Q[i]))
    else:
        print('AXIS: {}'.format(Q[i]))