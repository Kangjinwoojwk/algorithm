def sol(value, n):
    global N, min_value, max_value
    if n == N:
        if value < min_value:
            min_value = value
        if value > max_value:
            max_value = value
        return
    for i in range(4):
        if i == 0 and cal[i]:
            cal[i] -= 1
            sol(value + number[n], n + 1)
            cal[i] += 1
        elif i == 1 and cal[i]:
            cal[i] -= 1
            sol(value - number[n], n + 1)
            cal[i] += 1
        elif i == 2 and cal[i]:
            cal[i] -= 1
            sol(value * number[n], n + 1)
            cal[i] += 1
        elif i == 3 and cal[i]:
            cal[i] -= 1
            if value < 0:
                sol(-(abs(value)//number[n]), n + 1)
            else:
                sol(value // number[n], n + 1)
            cal[i] += 1
for tc in range(1, int(input()) + 1):
    N = int(input())
    cal = list(map(int, input().split()))
    number = list(map(int, input().split()))
    min_value = 1 << 31
    max_value = -(1 << 31)
    sol(number[0], 1)
    print('#{} {}'.format(tc, max_value - min_value))
