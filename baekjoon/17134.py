import sys
sys.stdout = open('17134.txt', 'w')
from time import time
a = time()
ceh = [True] * 1000001
ceh[0] = ceh[1] = False
for i in range(2, 1001):
    if ceh[i] == False:
        continue
    for j in range(i << 1, 1000000, i):
        ceh[j] = False
print(time()-a)
prime = [i for i in range(1000000) if ceh[i]]
print(time()-a)
n = len(prime)
print(n)
cnt = [0] * 1000001
for i in range(n):
    if prime[i] > 5000:
        break
    it = prime[i] << 1
    for j in range(1, n):
        if it + prime[j] > 10000:
            break
        cnt[it + prime[j]] += 1
print(time()-a)
for i in range(100):
    print(cnt[i*100:i*100+100])

# for _ in range(int(input())):
#     print(cnt[int(input())])
