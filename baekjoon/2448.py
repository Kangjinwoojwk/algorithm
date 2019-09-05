def sol(start, end, end2):
    if end - start > 3:
        sol(start, ((start + end) // 2), end2 - ((end - start) // 2))
        sol((start + end) // 2, end, end2 - (end -start))
        sol((start + end) // 2, end, end2)
    else:
        data[start][end2 - 3] = data[start + 1][end2 - 2] = data[start + 1][end2 - 4] = \
            data[start + 2][end2 - 5] = data[start + 2][end2 - 4] = data[start + 2][end2 - 3] = \
            data[start + 2][end2 - 2] = data[start + 2][end2 - 1] = '*'
N = int(input())
data = [[' '] * (N * 2) for _ in range(N)]
sol(0, N, 2 * N)
for i in data:
    print(''.join(i[1:]))