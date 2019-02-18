arr = [[9, 20, 2, 18, 11],
       [19, 1, 25, 3, 21],
       [8, 24, 10, 17, 7],
       [15, 4, 16, 5, 6],
       [12, 13, 22, 23, 14]]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
test_arr = [[0] * 5 for i in range(5)]
test_arr_sum = 0
for x in range(len(arr)):
    for y in range(len(arr[x])):
        for I in range(4):
            testX = x + dx[I]
            testY = y + dy[I]
            if 0 <= testX < 5 and 0 <= testY < 5:
                test_arr[x][y] += abs(arr[x][y] - arr[testX][testY])
        test_arr_sum += test_arr[x][y]
print(test_arr_sum)
