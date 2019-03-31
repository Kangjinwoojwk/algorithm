N = int(input())
N %= 1500000
a, b = 0, 1
i = 0
while i < N:
    i += 1
    a, b = b, (a + b) % 1000000
print(a)
