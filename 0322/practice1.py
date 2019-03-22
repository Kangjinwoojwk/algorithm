def Selection_Sort(n):
    if n ==len(li):
        return
    idx = 0
    value = 2**30
    for i in range(n, len(li)):
        if li[i] < value:
            idx = i
            value = li[i]
    li[n], li[idx] = li[idx], li[n]
    print(li)
    Selection_Sort(n + 1)

li = list(map(int, input().split()))
print(li)
Selection_Sort(0)
print(li)