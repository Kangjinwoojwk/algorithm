li = [True] * 250001
li[0] = li[1] = False
for i in range(2, 501):
    j = 2
    while i * j <= 250000:
        li[i * j] = False
        j += 1
while True:
    a = int(input())
    if a == 0:
        break
    else:
        print(li[a + 1: (2 * a) + 1].count(True))