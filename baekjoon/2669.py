wall = [[0]*101 for i in range(101)]
for _ in range(4):
    x, y, x_, y_ = map(int, input().split())
    for i in range(x, x_):
        for j in range(y, y_):
            wall[i][j] = 1
myeon = 0
for i in range(101):
    for j in range(101):
        if wall[i][j] == 1:
            myeon += 1
print(myeon)
