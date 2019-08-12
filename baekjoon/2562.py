max_number = 0
idx = 0
for i in range(1, 10):
    a = int(input())
    if a > max_number:
        max_number = a
        idx = i
print(max_number)
print(idx)