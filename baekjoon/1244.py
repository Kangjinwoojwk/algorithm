N = int(input())
li = list(map(int, input().split()))
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    if a == 1:
        for i in range(b - 1, N, b):
            li[i] = (li[i] + 1) % 2
    else:
        b -= 1
        li[b] = (li[b] + 1) % 2
        for i in range(1, N):
            if 0 <= b - i and b + i < N and li[b - i] == li[b + i]:
                li[b - i] = li[b + i] = (li[b - i] + 1) % 2
            else:
                break
i = 0
while i < N:
    print(' '.join(list(map(str, li[i:i + 20]))))
    i += 20