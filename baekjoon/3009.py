ans_x, ans_y = 0, 0
for _ in range(3):
    x, y = map(int, input().split())
    ans_x ^= x
    ans_y ^= y
print(ans_x, ans_y)