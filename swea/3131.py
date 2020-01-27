esto = [True] * 1000001
esto[0] = False
esto[1] = False
i = 2
while i <= 1000:
    if esto[i]:
        j = i * 2
        while j <= 1000000:
            esto[j] = False
            j += i
    i += 1
es = [i for i in range(1000001) if esto[i]]
print(' '.join(map(str, es)))