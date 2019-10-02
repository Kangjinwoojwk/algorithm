N, S = map(int, input().split())
data = list(map(int, input().split()))
i = 0
j = 0
minLength = 1000000
s = 0
while i != N or s > S:
    if s < S:
        s += data[i]
        i += 1
    elif s >= S:
        s -= data[j]
        j += 1
    if s >= S:
        if i - j < minLength:
            minLength = i - j
if minLength == 1000000:
    minLength = 0
print(minLength)