def itoa(a):
    result = []
    while a:
        result.append(a % 10)
        a //= 10
    result.reverse()
    re = ''
    for i in result:
        re += chr(i+ord('0'))
    return re


num = 12345
A = itoa(num)
print(A)
