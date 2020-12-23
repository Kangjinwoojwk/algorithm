arr = [2, 5, 7, 8, 12, 16, 21, 23, 33, 39, 42, 45, 45, 49, 62, 88]


# def binary_search(arr, key):
#     start, end = 0, len(arr) - 1
#     while start <= end:
#         mid = (start + end) >> 1
#         if arr[mid] == key: return mid
#         elif arr[mid] > key: end = mid - 1
#         else: start = mid + 1
#     return -1


def binary_search(arr, start, end, key):
    if start > end: return -1
    mid = (start + end) >> 1
    if arr[mid] == key: return mid
    elif arr[mid] > key:
        return binary_search(arr, start, mid - 1, key)
    else:
        return binary_search(arr, mid + 1, end, key)
