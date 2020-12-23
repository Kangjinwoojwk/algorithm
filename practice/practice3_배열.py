arr = [[9, 20, 2, 18, 11],
       [19, 1, 25, 3, 21],
       [8, 24, 10, 17, 7],
       [15, 4, 16, 5, 6],
       [12, 13, 22, 23, 14]]
arr_temp = []
for i in arr:
    for j in i:
        arr_temp.append(j)
N = len(arr_temp)
i = 0
while i < N:
    j = N - 1
    while j > i:
        if arr_temp[j] < arr_temp[j - 1]:
            arr_temp[j], arr_temp[j - 1] = arr_temp[j - 1], arr_temp[j]
        j -= 1
    i += 1
for i in range(len(arr)):
    for j in range(len(arr)):
        arr[i][j] = 0
i = x = y = direction = 0
while i < 25:
    arr[x][y] = arr_temp[i]
    if direction == 0:
        if y == N - 1 or arr[x][y + 1] != 0:
            direction += 1
    elif direction == 1:
        if x == N - 1 or arr[x + 1][y] != 0:
            direction += 1
    elif direction == 2:
        if y == 0 or arr[x][y - 1] != 0:
            direction += 1
    elif direction == 3:
        if x == 0 or arr[x - 1][y] != 0:
            direction = 0
    if direction == 0:
        y += 1
    elif direction == 1:
        x += 1
    elif direction == 2:
        y -= 1
    elif direction == 3:
        x -= 1
    i += 1
for i in arr:
    print(i)
