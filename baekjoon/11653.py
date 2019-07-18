N = int(input())
if N == 1:
    exit()
for i in range(2, N + 1):
    while True:
        if N == 1:
            exit()
        elif N % i == 0:
            print(i)
            N //= i
        else:
            break



# erato = [True]*10000000
# erato[0] = erato[1] = False
# for i in range(2, 3163):
#     if erato[i]:
#         for j in range(i * 2, 10000000, i):
#             erato[j] = False
#     else:
#         continue
# erato[1] = True
# N = int(input())
# while not erato[N]:
#     for i in range(2, 10000000):
#         if erato[i] and not N % i:
#             N //= i
#             print(i)
#             break
# print(N)