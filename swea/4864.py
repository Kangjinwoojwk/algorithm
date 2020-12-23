import sys
sys.stdin = open('4864.txt', 'r')
sys.stdout = open('4864_out.txt', 'w')
T = int(input()) # 부르트 포스는 쉬우므로 보이어 무어로 구현
for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()
    N = len(str1)
    M = len(str2)
    ans = 0
    i = j = N - 1
    while i < M:
        if str1[j] != str2[i]:
            k = 1
            while str2[i] != str1[j - k] and k < N:
                k += 1
            i += k
        else:
            k = 1
            while str2[i - k] == str1[j - k] and k < N:
                k += 1
            if k == N:
                ans = 1
                break
            else:
                i += 1

    print('#{} {}'.format(test_case, ans))
