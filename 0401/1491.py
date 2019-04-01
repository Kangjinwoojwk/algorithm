import sys
sys.stdin = open('input.txt', 'r')
import math
for tc in range(1, int(input()) + 1):
    N, A, B = map(int, input().split())
    ans = A * N + B * N
    n = int(math.sqrt(N))
    n_ = n
    while 0 < n * n_ <= N:
        temp = A * (n - n_) + B * (N - n * n_)
        if temp < ans:
            ans = temp
        if (n + 1) * n_ > N:
            n_ -= 1
        else:
            n += 1
    print('#{} {}'.format(tc, ans))