import math
import time
a = list()
b = list()
c = list()
t = time.time()
for i in range(1000000):
    a.append(i)
at = time.time()
print(at - t)
a.reverse()
at_ = time.time()
print(at_ - at)
for i in range(100000):
    b.insert(0, i)
bt = time.time()
print(bt - at)
for i in range(100000):
    c = [0] + c
ct = time.time()
print(ct - bt)