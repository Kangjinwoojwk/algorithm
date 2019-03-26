result = [(i*(i + 1))//2 for i in range(65600)]
S = int(input())
for i in range(65600):
    if result[i] > S:
        print(i - 1)
        break