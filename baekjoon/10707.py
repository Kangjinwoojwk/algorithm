A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())
a = A * P
b = B
if P > C:
    b += (P-C) * D
print(min(a, b))