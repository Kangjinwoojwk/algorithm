import sys
# sys.stdin = open('17134.txt', 'r')
# sys.stdout = open('17134_w.txt', 'w')
from time import time
t = time()
ceh = [True] * 1000001
ceh[0] = ceh[1] = False
for i in range(2, 1001):
    if ceh[i] is False:
        continue
    for j in range(i << 1, 1000000, i):
        ceh[j] = False
print(time()-t)
a = ''.join(['1' if ceh[i] else '0' for i in range(3, 1000000, 2)])
b = ''.join(reversed(['1' if ceh[i] else '0' for i in range(2, len(a) + 2)]))
# print(time()-t)
cnt = [0] * 500000
for _ in range(int(sys.stdin.readline())):
    n = (int(sys.stdin.readline()) - 5) // 2
    print(str(bin(int(a[:n], 2) & int(b[-n:], 2))).count('1'))
print(time() - t)


# a = ''.join(['1' if ceh[i] else '0' for i in range(3, 1000000, 2)])
# b = ''.join(reversed(['1' if ceh[i] else '0' for i in range(2, len(a) + 2)]))
# print('\n'.join([str(str(bin(int(a[:i], 2) & int(b[-i:], 2))).count('1')) for i in range(1, 500000)]))
# for i in range(1, 500000):
#     print(str(bin(int(a[:i], 2) & int(b[-i:], 2))).count('1'))
# cnt = [str(bin(int(a[:i], 2) & int(b[-i:], 2))).count('1') for i in range(1, len(a) + 1)]

# for _ in range(int(sys.stdin.readline())):
#     n = (int(sys.stdin.readline()) - 5) // 2
#     if cnt[n] == 0:
#         cnt[n] = str(bin(int(a[:n], 2) & int(b[-n:], 2))).count('1')
#     print(cnt[n])
    # print(str(bin(int(a[:n], 2) & int(b[-n:], 2))).count('1'))
# print(time() - t)

# cnt = [0] * 1000001
# a = 0
# b = 0
# for i in range(7, 1000000, 2):
#     if ceh[(i // 2) - 1]:
#         a += 1 << ((i // 2) - 3)
#     # b = (b << 1) + ceh[i - 4]
#     # if ceh[i - 4]:
#     #     b += 1
#     # cnt[i] = str(bin(a & b)).count('1')
#     if i % 10000 == 1:
#         print(bin(a))
#         print(time() - t)


# while i * 2 + 3 < 1000000:
#     if ceh[i]:
#         a += (1 << (i - 2))
#     b <<= 1
#     if ceh[2 * i - 1]:
#         b += 1
#
#     # n = a & a
#     # while n:
#     #     n &= (n - 1)
#     #     cnt[2 * i + 3] += 1
#     i += 1
#     # if i % 10000 == 0:
#     #     print(time() - t)
# print(time()-t)




# a_chk = 2
# b_chk = 3
# a = 0
# get = 1
# b = 0
# for i in range(7, 1000000, 2):
#     if ceh[a_chk]:
#         a += get
#     get *= 2
#     a_chk += 1
#     if ceh[b_chk]:
#         b = (b << 1) + 1
#     else:
#         b = b << 1
#     b_chk += 2
#     cnt[i] = str(bin(a & b)).count('1')
#     if i % 100000 == 1:
#         print(time()-t)




# for i in range(7, 1000, 2):
#     print(i, end=':')
#     for j in prime:
#         if j > i:
#             break
#         if ceh[i - j]:
#             print('({}, {})'.format(j//2, i - j), end='  ')
#     print()


# for _ in range(int(input())):
#     print(cnt[int(input())])

# print(time()-a)
