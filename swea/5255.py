li = [1, 1, 3]
def sol(n):
    if n <= len(li) - 1:
        return li[n]
    a = sol(n - 1) + 2 * sol(n - 2) + sol(n - 3)
    li.append(a)
    return a
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print('#{} {}'.format(tc, sol(N)))