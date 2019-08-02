data = [int(input()) for _ in range(9)]
for i in range(9):
    for j in range(i, 9):
        if i == j:
            pass
        else:
            if sum(data) - data[i] - data[j] == 100:
                for k in range(9):
                    if k != i and k != j:
                        print(data[k])
                exit()