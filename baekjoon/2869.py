A, B, V = map(int, input().split())
day = (V - A - 1) // (A - B)
print(day + 2)