import sys
sys.stdin = open('4880.txt', 'r')
sys.stdout = open('4880_out.txt', 'w')


def fight(a, b):
    if gawi_bawi_bo[a - 1] == gawi_bawi_bo[b - 1]:
        return True
    elif gawi_bawi_bo[a - 1] == 1:
        if gawi_bawi_bo[b - 1] == 2:
            return False
        else:
            return True
    elif gawi_bawi_bo[a - 1] == 2:
        if gawi_bawi_bo[b - 1] == 1:
            return True
        else:
            return False
    elif gawi_bawi_bo[a - 1] == 3:
        if gawi_bawi_bo[b - 1] == 1:
            return False
        else:
            return True


def sol(people):
    n = len(people)
    if n == 1:
        return people[0]
    a = sol(people[:n // 2 + n % 2])
    b = sol(people[n // 2 + n % 2:])
    if fight(a, b):
        return a
    else:
        return b


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    gawi_bawi_bo = list(map(int, input().split()))
    people = [_ for _ in range(1, N + 1)]
    ans = sol(people)
    print(f'#{test_case} {ans}')
