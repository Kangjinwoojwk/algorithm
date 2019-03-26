def sol(n):
    if len(memo) > n:
        return memo[n]
    else:
        memo.append(sol(n - 1) + sol(n - 2) + sol(n - 3))
    return memo[n]
T = int(input())
memo = [0, 1, 2, 4]
for _ in range(T):
    print(sol(int(input())))