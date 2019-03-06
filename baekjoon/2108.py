# 제로 부터 다시 hellojdh
N = int(input())
li = [int(input()) for _ in range(N)]
li.sort()
di = {}
for i in li:
    if i in di:
        di[i] += 1
    else:
        di[i] = 1
m = max(di.values())
modes = sorted(i for i in di if di[i] == m)
mode = modes[1 % len(modes)]
print(int(((sum(li) * 2 +N)// N) // 2))
print(li[N // 2])
print(mode)
print(li[-1] - li[0])




# 제로 부터 다시
# N = int(input())
# li = {}
# min_value = 4000
# max_value = -4000
# m = 0
# sum_value = 0
# most_value = 0
# cnt = 0
# center = 0
# chk_many = False
# for _ in range(N):
#     a = int(input())
#     sum_value += a
#     if min_value > a:
#         min_value = a
#     if max_value < a:
#         max_value = a
#     if a in li:
#         li[a] += 1
#         if m < li[a]:
#             m = li[a]
#             chk_many = False
#         elif m == li[a]:
#             chk_many = True
#     else:
#         cnt += 1
#         li[a] = 1
#         if m < li[a]:
#             m = li[a]
#             chk_many = False
#         elif m == li[a]:
#             chk_many = True
# li2 = list(li)
# li2.sort()
# chk_cnt = 0
# li3 = [li[li2[i]] for i in range(cnt)]
# for i in range(cnt):
#     if m == li3[i] and chk_many:
#         chk_many = False
#     elif m == li3[i]:
#         most_value = li2[i]
#         break
#
# for i in range(cnt):
#     chk_cnt += li3[i]
#     if chk_cnt >= N//2:
#         center = li2[i]
#         break
# print(round(sum_value/N))
# print(center)
# print(most_value)
# print(max_value - min_value)


# 왜...틀리냐....
# N = int(input())
# li = [0]*8001
# m = 0
# for _ in range(N):
#     a = int(input()) + 4000
#     li[a] += 1
#     if li[a] > m:
#         m = li[a]
# sum_v = 0
# cnt = 0
# center = 0
# center_chk = True
# bin_v = 0
# bin_chk = 2
# minimum = 0
# minimum_chk = True
# maximum = 0
# for i in range(8002):
#     if li[i] != 0:
#         sum_v += i * li[i]
#         cnt += li[i]
#     if center_chk and cnt > N // 2 and li[i]:
#         center = i
#         center_chk = False
#     if bin_chk != 0 and li[i] == m:
#         bin_chk -= 1
#         bin_v = i
#     if minimum_chk and li[i]:
#         minimum = i
#         minimum_chk = False
#     maximum = i
#     if cnt == N:
#         break
# print(int(round((sum_v // N) - 4000)))
# print(center - 4000)
# print(bin_v - 4000)
# print(maximum - minimum)

