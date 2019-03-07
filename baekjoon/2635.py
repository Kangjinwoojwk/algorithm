T = int(input())
li = [[T] for _ in range(T + 1)]
for i in range(1, T + 1):
    li[i].append(i)
    a = li[i][-2] - li[i][-1]
    while a >= 0:
        li[i].append(a)
        a = li[i][-2] - li[i][-1]
max_len = max([len(li[i]) for i in range(T + 1)])
print(max_len)
for i in range(1, T + 1):
    if len(li[i]) == max_len:
        print(' '.join(list(map(str, li[i]))))
        break