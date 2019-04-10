def sol(x_s, x_e, y_s, y_e, size, x, y, cnt):
    if x_e - x_s == 1 and y_e - y_s == 1:
        return cnt
    x_n = (x_s + x_e) // 2
    y_n = (y_s + y_e) // 2
    size //= 4
    if x_s <= x < x_n and y_s <= y < y_n:
        return sol(x_s, x_n, y_s, y_n, size, x, y, cnt)
    else:
        cnt += size
    if x_s <= x < x_n and y_n <= y < y_e:
        return sol(x_s, x_n, y_n, y_e, size, x, y, cnt)
    else:
        cnt += size
    if x_n <= x < x_e and y_s <= y < y_n:
        return sol(x_n, x_e, y_s, y_n, size, x, y, cnt)
    else:
        cnt += size
    if x_n <= x < x_e and y_n <= y < y_e:
        return sol(x_n, x_e, y_n, y_e, size, x, y, cnt)
    else:
        cnt += size

li = list(map(int, input().split()))
print(sol(0, 2**li[0], 0, 2**li[0], (2**li[0]) ** 2, li[1], li[2], 0))