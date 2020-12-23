arr = [64, 25, 10, 22, 11]
N = len(arr)
for i in range(N-1):
    minIdx = i
    for j in range(minIdx + 1, N):
        if arr[minIdx] > arr[j]:minIdx = j
    arr[i], arr[minIdx] = arr[minIdx], arr[i]
print(arr)