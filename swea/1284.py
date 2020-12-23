import sys
sys.stdin = open('1284.txt', 'r')
sys.stdout = open('1284_out.txt', 'w')
T = int(input())
for test_case in range(1, T + 1):
    ans = 0
    p, q, r, s, w = map(int, input().split())
    A = p * w
    B = q
    if w > r:
        B += (w - r) * s
    if A >= B:
        print('#{} {}'.format(test_case, B))
    else:
        print('#{} {}'.format(test_case, A))