N, C = map(int, input().split())
timeline = [False] * (C + 1)
data = set()
for i in range(N):
    n = int(input())
    if n in data:
        continue
    data.add(n)
    for j in range(n, C + 1, n):
        timeline[j] = True
print(timeline.count(True))



# N, C = map(int, input().split())
# data = [int(input()) for _ in range(N)]
# ans = 0
# while C:
#     for i in data:
#         if not C % i:
#             ans += 1
#             break
#     C -= 1
# print(ans)