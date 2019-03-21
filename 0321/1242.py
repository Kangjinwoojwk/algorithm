import sys
sys.stdin = open('1242.txt', 'r')
decoding = {
    '0001101' : 0,'0011001' : 1,'0010011' : 2,'0111101' : 3,'0100011' : 4,
    '0110001' : 5,'0101111' : 6,'0111011' : 7,'0110111' : 8,'0001011' : 9,}
T = int(input())
for tc in range(1, T + 1):
    ans = 0
    N, M = map(int, input().split())
    code = set()
    get = set()
    for _ in range(N):
        data = int(input(), 16)
        if data != 0:
            temp = str(bin(data)).rstrip('0')[2:]
            if temp in get:
                continue
            get.add(temp)
            temp = ('0' * 50) + temp
            while temp:
                i = 0
                while True:
                    i += 1
                    tm = temp[(-56 * i)::i]
                    chk = list()
                    for j in range(8):
                        if tm[j*7:j*7 + 7] not in decoding:
                            break
                        chk.append(decoding[tm[j*7:j*7 +7]])
                    else:
                        temp = temp[:-56 * i].rstrip('0')
                        if ''.join(map(str, chk)) in code:
                            break
                        else:
                            code.add(''.join(map(str, chk)))
                        cnt = 0
                        for i in range(8):
                            if i % 2:
                                cnt += chk[i]
                            else:
                                cnt += chk[i] * 3
                        if cnt % 10 == 0:
                            ans += sum(chk)
                        break
    print('#{} {}'.format(tc, ans))



















# T = int(input())
# for tc in range(1, T + 1):
#     ans = 0
#     N, M = map(int, input().split())
#     data = [input() for _ in range(N)]
#     code = []
#     for i in range(N):
#         j = M - 1
#         dum = ''
#         while j >= 0:
#             if data[i][j] != '0':
#                 temp = 1
#                 for k in range(j - 13, 0, -14):
#                     dum = data[i][k: j + 1]
#                     if data[i][k - 1] == '0':
#                         break
#                 j -= 14 * temp
#                 if dum not in code:
#                     code.append(dum)
#                 continue
#             j -= 1
#     for i in range(len(code)):
#         code[i] = code[i].lstrip('0')
#         for j in range(0, len(code[i]), 14):
#             code[i] = '0' + code[i]
#         code[i] = '0' + code[i]
#     for i in code:
#         data = [coding[int(j)] if 47 < ord(j) < 58 else coding[ord(j) - 55] for j in i]
#         n = len(data) // 14
#         i = ''.join(data)
#         i = i.rstrip('0')
#         data = [i[j] for j in range(len(i)-1, -1, -n)]
#         data.reverse()
#         data = ''.join(data)
#         i = ''
#         n = len(data)
#         for j in range(8):
#             for k in range(10):
#                 if decoding[k] == data[n-((j+1)*7):n-(j*7)]:
#                     i = str(k) + i
#         chk = 0
#         for j in range(7):
#             if j % 2:
#                 chk += int(i[j])
#             else:
#                 chk += int(i[j]) * 3
#         if (chk + int(i[-1])) % 10:
#             pass
#         else:
#             ans += sum(map(int, list(i)))
#     print(ans)