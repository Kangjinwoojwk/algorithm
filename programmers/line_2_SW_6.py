def sol(size, number):
    for i in range(2 * n - 1):
        for j in range(x, x + size):
            ans[i][j] = '.'
    y = 0
    if sorting_way == 'MIDDLE':
        y = n - 1 - (size - 1)
    elif sorting_way == 'bottom':
        y = ((n - 1) * 2) - ((size - 1) * 2)
    for i in range(y, y + (size * 2) - 1):
        for j in range(x, x + size):
            if number == '0' or number == '2' or number == '3' or number == '5' or number == '7' or number == '8' or number == '9':
                if i == y:
                    ans[i][j] = '#'
            if number == '0' or number == '2' or number == '3' or number == '5' or number == '6' or number == '8' :
                if i == y + (size * 2) - 2:
                    ans[i][j] = '#'
            if number == '0' or number == '1' or number == '2' or number == '3' or number == '4' or number == '7' or number == '8' or number == '9':
                if j == x + size - 1 and i < y + size:
                    ans[i][j] = '#'
            if number == '0' or number == '1' or number == '3' or number == '4' or number == '5' or number == '6' or number == '7' or number == '8' or number == '9':
                if j == x + size - 1 and i >= y + size:
                    ans[i][j] = '#'
            if number == '2' or number == '3' or number == '4' or number == '5' or number == '6' or number == '8' or number == '9':
                if i == y + size - 1:
                    ans[i][j] = '#'
            if number == '0' or number == '4' or number == '5' or number == '6' or number == '8' or number == '9':
                if j == x and i < y + size:
                    ans[i][j] = '#'
            if number == '0' or number == '2' or number == '6' or number == '8':
                if j == x and i >= y + size:
                    ans[i][j] = '#'


N, sorting_way = input().split()
N = int(N)
data = [list(map(int, input().split())) for _ in range(N)]
n = max(data)[0]
wide = sum([(len(str(i[1])) * i[0] + len(str(i[1]))) for i in data]) - 1
ans = [[' '] * wide for _ in range(n * 2 - 1)]
x = 0
for ii in data:
    for jj in str(ii[1]):
        sol(ii[0], jj)
        x += (ii[0] + 1)
for ii in ans:
    print(''.join(ii))