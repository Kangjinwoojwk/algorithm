w, h = map(int, input().split())
x, y = map(int, input().split())
t = int(input())
x += t
y += t
x = x % (2 * w)
y = y % (2 * h)
if x > w:
    x = 2 * w - x
if y > h:
    y = 2 * h - y
print(x, y)