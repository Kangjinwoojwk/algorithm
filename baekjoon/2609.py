A, B = map(int, input().split())
a, b = A, B
while a != 0 and b != 0:
    if a < b:
        a, b = b, a
    a -= b
print(a + b)
print((A * B)//(a + b))