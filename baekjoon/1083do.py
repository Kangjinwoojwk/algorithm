N = int(input())
li = list(map(int, input().split()))
S = int(input())
idx = 0
while S:
    if idx == N:
        break
    i = li.index(max(li[idx: idx + S + 1]))
    li.insert(idx, li.pop(i))
    S -= (i - idx)
    idx += 1
print(' '.join(map(str, li)))
