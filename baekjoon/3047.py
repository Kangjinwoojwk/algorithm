li = list(map(int, input().split()))
li.sort()
chk = ['A', 'B', 'C']
a = input()
for i in range(3):
    for j in range(3):
        if a[i] == chk[j]:
            print(li[j], end='')
    if i != 2:
        print(' ', end='')