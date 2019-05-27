F = [0, 1]
Flen = [1, 1]
for i in range(2, 101):
    Flen.append(Flen[i - 1] + Flen[i - 2])
print(F)
print(Flen)

while True:
    try:
        a, b = '0', '1'
        n = int(input())
        p = input()
        for i in range(n):
            a, b = b, b + a

    except EOFError:
        break