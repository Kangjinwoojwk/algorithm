# 부분집합 합 문제 구현
# 부분집합의 합이 10이 되는 것만 출력하는 것을 제작해 보자.
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(arr)
for i in range(1 << N):
    sum_v = 0
    for j in range(N):
        if i & (1 << j):
            sum_v += arr[j]
    if sum_v == 10:
        for j in range(N):
            if i & (1 << j):
                print(arr[j], end=',')
        print()






# arr = [3, 6, 7, 1, 5, 4]
# n = len(arr)
# for i in range(1 << n):
#     for j in range(n):
#         if i & (1 << j):
#             print(arr[j], end=', ')
#     print()
# print()

# arr = [1, 3, 5]
# bit = [0] * len(arr)
# for i in [0, 1]:
#     bit[0] = i
#     for j in [0, 1]:
#         bit[1] = j
#         for k in [0, 1]:
#             bit[2] = k
#             print(bit)