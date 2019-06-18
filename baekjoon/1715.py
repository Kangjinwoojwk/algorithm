import heapq
data = list()
n = int(input())
for i in range(n):
    heapq.heappush(data, int(input()))
ans = 0
while n > 1:
    temp = heapq.heappop(data) + heapq.heappop(data)
    ans += temp
    heapq.heappush(data, temp)
    n -= 1
print(ans)

# n = int(input())
# data = list()
# for i in range(n):
#     temp = int(input())
#     for j in range(len(data)):
#         if data[j] > temp:
#             data.insert(j, temp)
#             break
#     else:
#         data.append(temp)
# ans = 0
# if n < 2:
#     print(ans)
#     exit()
# else:
#     while len(data) >= 2:
#         temp = data.pop(0) + data.pop(0)
#         ans += temp
#         for i in range(len(data)):
#             if data[i] > temp:
#                 data.insert(i, temp)
#                 break
#         else:
#             data.append(temp)
#     print(ans)