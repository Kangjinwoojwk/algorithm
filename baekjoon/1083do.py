N = int(input())
li = input().split()
S = int(input())
while S:
    for i in range(N):
        idx = li.index(max(li[i:i + S + 1]))
        if idx == i:
            if i == N - 1:
                S = 0
            continue
        li = li[:i] + [li[idx]] + li[i:idx] + li[idx + 1:]
        S -= (idx - i)
        break
print(' '.join(li))
