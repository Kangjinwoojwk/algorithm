li = [True] * 10001
li[0] = li[1] = False
for i in range(2, 100):
    j = 2
    while i * j <= 10000:
        li[i * j] = False
        j += 1
T = int(input())
for _ in range(T):
    a = int(input())
    for i in range(a//2, 1, -1):
        if li[i] and li[a - i]:
            print(i, a - i)
            break