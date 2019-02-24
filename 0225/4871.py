import sys
sys.stdin = open('4871.txt', 'r')
sys.stdout = open('4871_out.txt', 'w')

T = int(input())
for test_case in range(1, T + 1):
    V, E = list(map(int, input().split()))
    li = [list(map(int, input().split()))for _ in range(E)]
    line = [[] for _ in range(V + 1)]
    for i in range(E):
        line[li[i][0]].append(li[i][1])
        line[li[i][1]].append(li[i][0])
    S, G = list(map(int, input().split()))
    chk = [False] * (V + 1)
    chk[S] = True
    def sol(S):
        global G
        if chk[G]:
            return
        for i in line[S]:
            if chk[i] == False:
                chk[i] = True
                sol(i)
    sol(S)
    if chk[G]:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')





# T = int(input())
# for test_case in range(1, T + 1):
#     V, E = list(map(int, input().split()))
#     li = [list(map(int, input().split()))for _ in range(E)]
#     S, G = list(map(int, input().split()))
#     chk = [False] * (V + 1)
#     chk[S] = True
#
#
#     def sol(S):
#         global G
#         if chk[G]:
#             return
#         for i in li:
#             if i[0] == S:
#                 if chk[i[1]]:
#                     pass
#                 else:
#                     chk[i[1]] = True
#                     sol(i[1])
#     sol(S)
#     if chk[G]:
#         print(f'#{test_case} 1')
#     else:
#         print(f'#{test_case} 0')

