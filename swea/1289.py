import sys
sys.stdin = open('1289.txt', 'r')
T = int(input())
for tc in range(1, T + 1):
    data = list(map(int, list(input())))
    ptr = 0
    ans = 0
    for i in data:
        if i != ptr:
            ptr = (ptr + 1) % 2
            ans += 1
    print('#{} {}'.format(tc, ans))
