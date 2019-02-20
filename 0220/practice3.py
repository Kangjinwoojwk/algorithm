p = 'CATTCCCTGCGCCGC'
t = 'ATTGTGATGTTTGAGCTTTTACGTAGAGAAACTGAACGTACCTACGACATTCCCTGCGCCGCCACCCGCTTTTTGACATTCCCTGCGCCGC'
n, m = len(t), len(p)

i = 0
while i <= n - m:
    j = 0
    while j < m:
        if t[i + j] != p[j]:
            break
        j += 1
    if j == m:
        print(i, i + m - 1)
        i += m
    i += 1
