li = [list(input()) for _ in range(5)]
result = list()
while li[0] or li[1] or li[2] or li[3] or li[4]:
    for i in range(5):
        if li[i]:
            result.append(li[i].pop(0))
print(''.join(result))
