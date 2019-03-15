number = [i for i in range(10001)]
for i in range(1, 10001):
    n = i
    while i:
        n += i % 10
        i //= 10
    if n < 10001:
        number[n] = 0
print('\n'.join([str(number[i]) for i in number if number[i]]))