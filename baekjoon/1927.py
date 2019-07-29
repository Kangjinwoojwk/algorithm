import sys
import heapq
data = list()
for _ in range(int(sys.stdin.readline())):
    a = int(sys.stdin.readline())
    if a == 0:
        if data:
            print(heapq.heappop(data))
        else:
            print(0)
    else:
        heapq.heappush(data, a)