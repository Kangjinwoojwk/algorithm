# 대각선으로 순회, 사선 개수는 가운데 중복 빼고 열수 + 행수 - 1
# 사선 시작 위치는 'ㄱ'으로 보인다.
arr = [[1, 2, 4, 7, 11],
       [3, 5, 8, 12, 15],
       [6, 9, 13, 16, 18],
       [10, 14, 17, 19, 20]]
N, M = len(arr), len(arr[0])
for diag in range(N + M - 1):
    x = 0 if diag < M else diag - M + 1
    y = diag if diag < M else M - 1
    while x < N and y >= 0:
        print(arr[x][y])
        x, y = x + 1, y - 1
