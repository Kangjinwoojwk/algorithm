N = int(input())
data = input()
check = [0, 0]
for i in data:
    if i == 'A':
        check[0] += 1
    elif i == 'B':
        check[1] += 1
if check[0] > check[1]:
    print('A')
elif check[0] < check[1]:
    print('B')
else:
    print('Tie')