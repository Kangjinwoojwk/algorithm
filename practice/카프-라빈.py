p = 'CATTCCCTGCGCCGC'
t = 'ATTGTGATGTTTGAGCTTTTACGTAGAGAAACTGAACGTACCTACGACATTCCCTGCGCCGCCACCCGCTTTTTGACATTCCCTGCGCCGC'
n, m = len(t), len(p)

th, ph, h0 = 0, 0, 1 # 타입 해쉬, 패턴해쉬
for i in range(m):
    th = (th * 10 + ord(t[i])) % 12345
    ph = (ph * 10 + ord(p[i])) % 12345
for i in range(m - 1):
    h0 = (h0 * 10) % 12345

for i in range(n - m + 1):
    if ph == th:
        j = 0
        while j < m:
            if t[i + j] != p[j]: break
            j += 1
        if j == m:
            print(t[i:])
            break
    if i == n - m: break
    th = (th - ord(t[i]) * h0) * 10 + ord(t[i - m]) % 12345
