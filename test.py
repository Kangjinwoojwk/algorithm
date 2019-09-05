import math
import time
import sys
sys.setrecursionlimit(200000)
def sol(n):
    if n == 10:
        return
    for i in range(10):
        if visit[i]:
            visit[i] = False
            a[n] = i
            sol(n + 1)
            visit[i] = True
a = [0]*10
visit = [True] * 10
t = time.time()
sol(0)
at = time.time()
print(at - t)

bt = time.time()
print(bt - at)