str1 = list('algorithm')
cnt = len(str1) // 2
for i in range(cnt):
    str1[i], str1[-i-1] = str1[-i-1], str1[i]
print(''.join(str1))