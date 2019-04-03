import sys
for _ in range(int(sys.stdin.readline())):
    a, b = sys.stdin.readline().split()
    a = int(a)
    a -= 1
    ans = 0
    for i in b:
        ans += ord(i) - 48
        ans %= a
    print(ans)
# for _ in range(int(input())):
#     a, b = input().split()
#     a = int(a) - 1
#     ans = 0
#     for i in b:
#         ans += int(i)
#         ans %= a
#     print(ans)


# for _ in range(int(input())):
#     a, b = map(int, input().split())
#     a -= 1
#     ans = 0
#     while b:
#         ans += b % 10
#         b //= 10
#     print(ans % a)


# for _ in range(int(input())):
#     a, b = input().split()
#     a = int(a)
#     b = list(map(int, list(b)))
#     b = sum(b)
#     print(b % (a - 1))

# for _ in range(int(input())):
#     a, b = input().split()
#     a = int(a)
#     b = int(b, a)
#     print(b % (a - 1))