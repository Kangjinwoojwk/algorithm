A = [0]*26
for i in input():
    A[ord(i)-ord('a')] += 1
print(' '.join(map(str, A)))