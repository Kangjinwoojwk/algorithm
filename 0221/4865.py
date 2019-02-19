import sys
sys.stdin = open('4865.txt', 'r')
sys.stdout = open('4865_out.txt', 'w')
T = int(input())
for test_case in range(1, T + 1):
    str1, str2 = input(), input()
    N, M = len(str1), len(str2)
    li = [0] * 26
    li_chk = [False] * 26
    for i in range(N):
        li_chk[ord(str1[i])-65] = True
    for i in range(M):
        if li_chk[ord(str2[i])-65]:
            li[ord(str2[i])-65] += 1
    Max_count = 0
    for i in range(26):
        if li[i] > Max_count:
            Max_count = li[i]
    print(f'#{test_case} {Max_count}')
