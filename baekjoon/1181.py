N = int(input())
li = []
chk = set()
for _ in range(N):
    a = input()
    if a in chk:
        continue
    chk.add(a)
    li.append([len(a), a])
li.sort()
li = [i[1] for i in li]
print('\n'.join(li))