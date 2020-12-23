T = list(input())
T = [int(i) if 47 < ord(i) < 58 else ord(i) - 55 for i in T]
result = [''] * len(T)
for idx, value in enumerate(T):
    for j in range(4):
        result[idx] = str(value % 2) + result[idx]
        value //= 2
result = ''.join(result)
li = [0] * (len(result)//7 + 1)
for idx, v in enumerate(result):
    if v == '1':
        li[idx//7] += 2**(6 - (idx % 7))
if len(result) % 7 == 0:
    pass
else:
    li[-1] //= 2**(7 - len(result) % 7)
print(' '.join(map(str, li)))