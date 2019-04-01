li = list()
li.append(1)
for i in range(1, 10001):
    a = li[i - 1]*i
    li.append(a)
while True:
    try:
        a = input()
        print(' ' * (5 - len(a)) + a, '->', str(li[int(a)]).rstrip('0')[-1])
    except EOFError:
        break