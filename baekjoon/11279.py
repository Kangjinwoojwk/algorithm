import sys
import heapq
data = list()
for _ in range(int(sys.stdin.readline())):
    a = int(sys.stdin.readline())
    if a == 0:
        if data:
            print(-heapq.heappop(data))
        else:
            print(0)
    else:
        heapq.heappush(data, -a)

# 시간 초과
# heap = list()
# for _ in range(int(input())):
#     a = int(input())
#     if a == 0:
#         if heap:
#             print(heap.pop(0))
#         else:
#             print(0)
#     else:
#         for i in range(len(heap)):
#             if heap[i] < a:
#                 heap.insert(i, a)
#                 break
#         else:
#             heap.append(a)