def sol(n):
    if n <= 2:
        return n
    elif n == 3:
        return 4
    return sol(n - 1) + sol(n - 2) + sol(n - 3)
T = int(input())
for _ in range(T):
    print(sol(int(input())))