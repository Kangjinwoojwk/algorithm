a, b = input().split()
a_c = b_c = 0
a_len = len(a)
b_len = len(b)
for i in range(a_len):
    for j in range(b_len):
        if a[i] == b[j]:
            a_c = i
            b_c = j
            break
    else:
        continue
    break
li = [['.'] * a_len for _ in range(b_len)]
for i in range(a_len):
    li[b_c][i] = a[i]
for i in range(b_len):
    li[i][a_c] = b[i]
for i in range(b_len):
    print(''.join(li[i]))