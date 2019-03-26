N = input()
for i in range(1, len(N)):
    value1 = 1
    value2 = 1
    for j in range(i):
        value1 *= int(N[j])
    for j in range(i, len(N)):
        value2 *= int(N[j])
    if value1 == value2:
        print('YES')
        break
else:
    print('NO')