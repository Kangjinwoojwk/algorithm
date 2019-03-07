value = 0
chk = True
for _ in range(10):
    a = int(input())
    if chk and abs(value + a - 100) <= abs(value - 100):
        value += a
    else:
        chk = False
print(value)