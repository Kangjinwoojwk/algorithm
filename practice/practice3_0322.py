def sol(n):
    if n == len(li):
        if sum(result) == 0:
            print(result)
        return
    result.append(li[n])
    sol(n + 1)
    result.pop(-1)
    sol(n + 1)
li = list(map(int, input().split()))
result = []
sol(0)