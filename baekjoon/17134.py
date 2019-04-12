import sys
# sys.stdin = open('17134.txt', 'r')
sys.stdout = open('17134_w.txt', 'w')
from time import time
a = time()
ceh = [True] * 1000001
ceh[0] = ceh[1] = False
for i in range(2, 1001):
    if ceh[i] is False:
        continue
    for j in range(i << 1, 1000000, i):
        ceh[j] = False
print(time()-a)
prime = [i * 2 for i in range(1000001) if ceh[i]]
print(time()-a)
cnt = [0] * 1000001
for i in range(7, 1000, 2):
    print(i, end=':')
    for j in prime:
        if j > i:
            break
        if ceh[i - j]:
            print('({}, {})'.format(j//2, i - j), end='  ')
    print()


# for _ in range(int(input())):
#     print(cnt[int(input())])

# print(time()-a)
