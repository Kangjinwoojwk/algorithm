import sys
sys.stdin = open('4880.txt', 'r')
sys.stdout = open('4880_out.txt', 'w')

def sol(gawi_bawi_bo, people):
    n = len(people)
    if n == 1:
        return
    N = n // 2
    for i in range(N-1, -1, -1):
        if gawi_bawi_bo[2 * i] == gawi_bawi_bo[2 * i + 1]:
            gawi_bawi_bo[:] = gawi_bawi_bo[:2 * i + 1] + gawi_bawi_bo[2 * i + 2:]
            people[:] = people[:2 * i + 1] + people[2 * i + 2:]
        elif gawi_bawi_bo[2 * i + 1] == 3 and gawi_bawi_bo[2 * i] == 1:
            gawi_bawi_bo[:] = gawi_bawi_bo[:2 * i + 1] + gawi_bawi_bo[2 * i + 2:]
            people[:] = people[:2 * i + 1] + people[2 * i + 2:]
        elif gawi_bawi_bo[2 * i + 1] < gawi_bawi_bo[2 * i]:
            gawi_bawi_bo[:] = gawi_bawi_bo[:2 * i + 1] + gawi_bawi_bo[2 * i + 2:]
            people[:] = people[:2 * i + 1] + people[2 * i + 2:]
        else:
            gawi_bawi_bo[:] = gawi_bawi_bo[:2 * i] + gawi_bawi_bo[2 * i + 1:]
            people[:] = people[:2 * i] + people[2 * i + 1:]
    sol(gawi_bawi_bo, people)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    gawi_bawi_bo = list(map(int, input().split()))
    people = [i for i in range(1, N + 1)]
    sol(gawi_bawi_bo, people)
    print(f'#{test_case} {people[0]}')