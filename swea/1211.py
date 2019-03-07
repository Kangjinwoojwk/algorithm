import sys
sys.stdin = open('1211.txt', 'r')
def get_distance(x, y, step):
    if x == 99:
        return step
    if y + 1 < 100 and laddar[x][y + 1] == '1':
        i = 1
        while y + i + 1 < 100 and laddar[x][y + i + 1] == '1':
            i += 1
        return get_distance(x + 1, y + i, step + i + 1)
    elif 0 <= y - 1 and laddar[x][y - 1] == '1':
        i = 1
        while 0 <= y - i - 1 and laddar[x][y - i - 1] == '1':
            i += 1
        return get_distance(x + 1, y - i, step + i + 1)
    else:
        return get_distance(x + 1, y, step + 1)

for _ in range(10):
    tc = int(input())
    laddar = [input().split() for _ in range(100)]
    ans = 0
    min_distance = 1 << 30
    for i in range(100):
        if laddar[0][i] == '1':
            distance = get_distance(0, i, 1)
            if distance <= min_distance:
                min_distance = distance
                ans = i
    print('#{} {}'.format(tc, ans))