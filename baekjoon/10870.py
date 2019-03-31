N = int(input())
a, b = 0, 1
i = 0
while i < N:
    i += 1
    a, b = b, a + b
print(a)