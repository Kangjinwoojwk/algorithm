import sys
sys.stdin = open('6190.txt', 'r')
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    chk = 0
    ans = -1
    for i in range(N):
        for j in range(i + 1, N):
            chk = data[i] * data[j]
            if chk > ans:
                li = list(str(chk))
                len_list = len(li)
                for k in range(len_list - 1):
                    if li[k] > li[k + 1]:
                        break
                else:
                    ans = chk
    print('#{} {}'.format(tc, ans))