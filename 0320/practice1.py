T = input()
li = [0] * (len(T) // 7)
for idx, v in enumerate(T):
    if v == '1':
        li[idx//7] += 2**(6 - (idx % 7))
print(' '.join(map(str, li)))
