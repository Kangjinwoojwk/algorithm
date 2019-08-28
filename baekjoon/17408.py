N = int(input())
data = list(map(int, input().split()))
M = int(input())
for _ in range(M):
    q, a, b = map(int, input().split())
    a -= 1
    if q == 1:
        data[a] = b
    else:
        c = d = 0
        for i in range(a, b):
            if data[i] >= c:
                c, d = data[i], c
            elif data[i] > d:
                d = data[i]
        print(c + d)

# 시간초과 당연히 2번 쿼리쪽이 문제인듯
# N = int(input())
# data = list(map(int, input().split()))
# M = int(input())
# for _ in range(M):
#     q, a, b = map(int, input().split())
#     a -= 1
#     if q == 1:
#         data[a] = b
#     else:
#         temp = data[a: b]
#         temp.sort()
#         print(temp[-1] + temp[-2])