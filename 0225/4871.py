import sys
sys.stdin = open('4871.txt', 'r')
sys.stdout = open('4871_out.txt', 'w')
T = int(input())

for test_case in range(1, T + 1):
    V, E = list(map(int, input().split()))
    li = [list(map(int, input().split()))for _ in range(E)]
    S, G = list(map(int, input().split()))
    chk = [False] * (V + 1)
    chk[S] = True


    def sol(S, chk, li):
        for i in li:
            if i[0] == S:
                if chk[i[1]]:
                    pass
                else:
                    chk[i[1]] = True
                    sol(i[1], chk, li)
    sol(S, chk, li)
    if chk[G]:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')

