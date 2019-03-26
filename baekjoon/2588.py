A = int(input())
B = int(input())
final = A * B
for i in range(len(str(B))):
    print(A * (B % 10))
    B //= 10
print(final)
