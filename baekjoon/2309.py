def sol(n):
    if n == 9:
        if len(result) == 7 and sum(result) == 100:
            result.sort()
            print('\n'.join(map(str, result)))
            exit()
        return
    result.append(li[n])
    sol(n + 1)
    result.pop()
    sol(n + 1)

li = [int(input()) for _ in range(9)]
result = []
sol(0)