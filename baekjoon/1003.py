def sol(n):
    if n < len(li):
        return li[n]
    else:
        a1, b1 = sol(n - 1)
        a2, b2 = sol(n - 2)
        li.append((a1 + a2, b1 + b2))
        return li[n]

li = [(1, 0), (0, 1)]
T = int(input())
for _ in range(T):
    N = int(input())
    a, b = sol(N)
    print(a, b)
