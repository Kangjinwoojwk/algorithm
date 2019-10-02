N, M = map(int, input().split())
data = list(map(int, input().split()))
ans = 0
i = 0
j = 0
s = 0
while j < N:
    if s <= M:
        s += data[j]
        j += 1
    elif s > M:
        s -= data[i]
        i += 1
    if s == M:
        ans += 1
while s > M:
    s -= data[i]
    i += 1
    if s == M:
        ans += 1
print(ans)

# N, M = map(int, input().split())
# data = list(map(int, input().split()))
# ans = 0
# for i in range(N):
#     for j in range(i + 1, N + 1):
#         if sum(data[i:j]) == M:
#             ans += 1
# print(ans)
