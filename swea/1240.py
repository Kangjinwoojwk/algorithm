import sys
sys.stdin = open('1240.txt', 'r')
T = int(input())
decoding = ['0001101', '0011001', '0010011', '0111101', '0100011',
            '0110001', '0101111', '0111011', '0110111', '0001011']
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]
    code = ''
    for i in range(N):
        if code != '':
            break
        for j in range(M - 1, -1, -1):
            if data[i][j] == '1':
                for k in range(7, 63, 7):
                    for l in range(10):
                        if decoding[l] == data[i][j - k + 1:j - k + 8]:
                            code = str(l)+code
                else:
                    break
    chk = 0
    for i in range(7):
        if i % 2:
            chk += int(code[i])
        else:
            chk += int(code[i]) * 3
    if (chk + int(code[-1])) % 10:
        print('#{} 0'.format(tc))
    else:
        print('#{} {}'.format(tc,sum(map(int, list(code)))))

