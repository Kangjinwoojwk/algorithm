li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(1<<len(li)):
    sum_v = 0
    for j in range(len(li)):
        if i & 1 << j:
            sum_v += li[j]
    else:
        if sum_v == 10:
            for j in range(len(li)):
                if i & 1 << j:
                    print(li[j], end=' ')
            print()
