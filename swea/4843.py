import sys
sys.stdin = open('4843.txt', 'r')
sys.stdout = open('4843_output', 'w')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    i = 0
    while i < N:
        j = N - 1
        while j > i:
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]
            j -= 1
        i += 1
    print(f'#{test_case}', end=' ')
    for i in range(5):
        print(f'{A[-1 - i]} {A[0 + i]}', end=' ')
    print()
