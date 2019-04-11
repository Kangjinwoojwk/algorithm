# import sys
# sys.stdin = open('17134.txt', 'r')
# sys.stdout = open('17134_w.txt', 'w')
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
prime = [i for i in range(1000000) if ceh[i]]
print(time()-a)
cnt = [0] * 1000001

# for _ in range(int(input())):
#     print(cnt[int(input())])

# print(time()-a)
