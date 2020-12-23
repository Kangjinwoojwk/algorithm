import sys
sys.stdin = open('1220.txt', 'r')
sys.stdout = open('1220_out', 'w')
for t in range(1, 11):
    N = int(input())
    m = [input().split() for _ in range(N)]
    a = 0
    for i in range(N):
        c = 0
        for j in range(N):
            if m[j][i] == '1':
                c = 1
            elif m[j][i] == '2' and c == 1:
                a += 1
                c = 0
    print('#{} {}'.format(t, a))
