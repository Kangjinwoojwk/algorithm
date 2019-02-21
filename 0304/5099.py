import sys
sys.stdin = open('5099.txt', 'r')
sys.stdout = open('5099_out.txt', 'w')
T = int(input())
for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    li = list(map(int, input().split()))
    li_num = [i for i in range(1, M + 1)]
    oven = [[li[_], li_num[_]] for _ in range(N)]
    li = li[N:]
    li_num = li_num[N:]
    while len(li) != 0 or len(oven) != 1:
        oven[0][0] //= 2
        if oven[0][0] == 0:
            if len(li):
                oven[0][0] = li[0]
                oven[0][1] = li_num[0]
                li = li[1:]
                li_num = li_num[1:]
            else:
                oven = oven[1:]
                continue
        oven = oven[1:] + [oven[0]]
    print(f'#{test_case} {oven[0][1]}')





