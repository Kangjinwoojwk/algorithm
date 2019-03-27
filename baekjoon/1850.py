A, B = map(int, input().split())
if A > B:
    A, B = B, A
while A:
    B -= (B//A) * A
    A, B = B, A
print('1' * B)