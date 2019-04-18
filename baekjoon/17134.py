import sys
sys.stdin = open('17134.txt', 'r')
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
print(ceh.count(True))
# a = int(''.join(['1' if ceh[i] else '0' for i in range(3, 1000000, 2)]), 2)
# b = int(''.join(reversed(['1' if ceh[i] else '0' for i in range(2, 500001)])), 2)
# cnt = [bin(a & b << n).count('1') for n in range(499999, -1, -1)]
# print(time()-t)

# a = [ceh[i] for i in range(3, 1000000, 2)]
# b = list(reversed([ceh[i] for i in range(2, len(a) + 2)]))
# cnt = [len([True for i in range(n) if a[i] and b[-(n - i)]]) for n in range(500000)]
# print(time()-t)


# a = int(''.join(['1' if ceh[i] else '0' for i in range(3, 1000000, 2)]), 2)
# b = int(''.join(reversed(['1' if ceh[i] else '0' for i in range(2, 500001)])), 2)
# print(time()-t)
# cnt = [bin((a >> n) & b).count('1') for n in range(499998, -1, -1)]
# a = int(''.join(['1' if ceh[i] else '0' for i in range(3, 1000000, 2)]), 2)
# b = int(''.join(reversed(['1' if ceh[i] else '0' for i in range(2, 500001)])), 2)
# a = int(''.join(['1' if ceh[i] else '0' for i in range(3, 1000000, 2)]), 2)
# b = int(''.join(reversed(['1' if ceh[i] else '0' for i in range(2, 500001)])), 2)
# cnt = [bin((a >> n) & b).count('1') for n in range(499999, -1, -1)]
# print(cnt)
# print(time()-t)
# a = 0
# b = 0
# cnt = list()
# for i in range(500000):
#     a <<= 1
#     if ceh[i * 2 + 1]:
#         a += 1
#     b += ceh[i + 2] << i
#     cnt.append(bin(a & b))
# print(time()-t)


# result = list()
# for _ in range(int(sys.stdin.readline())):
#     n=(int(sys.stdin.readline()) - 7) // 2
#     result.append(len([True for i in range(n) if a[i] and b[-(n - i)]]))
# print(' '.join(map(str, result)))




# a = 0
# b = 0
# for i in range(500000):
#     a |= ceh[2 * i + 1] << i
#     b |= ceh[i + 2] << i


# t = time()
# cnt = [len([True for i in range(n) if a[i] and b[-(n - i)]]) for n in range(50000)]
# print(time() - t)
# t = time()
# for _ in range(int(sys.stdin.readline())):
#     n = (int(sys.stdin.readline()) - 7) // 2
#     len([True for i in range(n) if a[i] and b[-(n - i)]])
# print(time() - t)

# a = int(''.join(['1' if ceh[i] else '0' for i in range(3, 1000000, 2)]), 2)
# b = int(''.join(reversed(['1' if ceh[i] else '0' for i in range(2, 500001)])), 2)
# cnt = [bin((a >> n) & b).count('1') for n in range(499999, -1, -1)]
# len:499999
# for _ in range(int(sys.stdin.readline())):
#     print(cnt[(int(sys.stdin.readline()) - 7) // 2])


# print(sum([True if a[i] and b[-(n - i)] else False for i in range(n)]))
# print(str(bin(int(a[:n], 2) & int(b[-n:], 2))).count('1'))
# a = [ceh[i] for i in range(3, 1000000, 2)]
# b = list(reversed([ceh[i] for i in range(2, len(a) + 2)]))
# cnt = [len([True for i in range(n) if a[i] and b[-(n - i)]]) for n in range(50000)]
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
