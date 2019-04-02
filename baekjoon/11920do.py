N, K = map(int, input().split())
li = list(map(int, input().split()))
H = list()
cnt = 0
i = 0
while i < N:
    if cnt < K:
        H.append(li.pop(i))
        cnt += 1
        N -= 1
        for j in range(cnt - 1, 0, -1):
            if H[j - 1] > H[j]:
                H[j - 1], H[j] = H[j], H[j - 1]
            else:
                break
    elif H[0] < li[i]:
        H.append(li.pop(i))
        for j in range(cnt - 1, 0, -1):
            if H[j - 1] > H[j]:
                H[j - 1], H[j] = H[j], H[j - 1]
            else:
                break
        li[i:i] = [H.pop(0)]
        i += 1
    else:
        i += 1
li.extend(H)
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