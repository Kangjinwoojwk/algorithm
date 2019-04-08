a = input()
for i in range(len(a) // 2):
    if a[i] != a[-1 - i]:
        print(0)
        break
else:
    print(1)