import sys
from queue import PriorityQueue
N, K = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
H = PriorityQueue()
i = 0
while i < N:
    if H.qsize() < K:
        H.put(li.pop(i))
        N -= 1
        continue
    else:
        temp = H.get()
        if temp < li[i]:
            temp, li[i] = li[i], temp
        H.put(temp)
    i += 1
for i in range(K):
    li.append(H.get())
print(' '.join(map(str, li)))




# class heap:
#     def __init__(self):
#         self.li = list()
#         self.cnt = 0
#     def top(self):
#         return self.li[0]
#     def get(self, a):
#         self.li.append(a)
#         b = self.cnt
#         while b:
#             if self.li[b - 1] > self.li[b]:
#                 self.li[b - 1], self.li[b] = self.li[b], self.li[b - 1]
#                 b -= 1
#             else:
#                 break
#         self.cnt += 1
#     def pop(self):
#         self.cnt -= 1
#         return self.li.pop(0)
#     def len(self):
#         return self.cnt
# N, K = map(int, input().split())
# li = list(map(int, input().split()))
# H = heap()
# i = 0
# while i < N:
#     if H.len() < K:
#         H.get(li.pop(i))
#         N -= 1
#     elif H.top() < li[i]:
#         a = H.pop()
#         li[i], a = a, li[i]
#         H.get(a)
#         i += 1
#     else:
#         i += 1
# for i in range(K):
#     li.append(H.pop())
# print(li)