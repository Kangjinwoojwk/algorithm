N = int(input())
data = list(map(int, input().split()))
A = [0] * 1001
for i in data:
    a = max(A[:i])
    if a == 0:
        A[i] = 1
    else:
        A[i] = a + 1
print(max(A))