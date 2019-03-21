def quick_sort(li):
    if len(li) <= 1:
        return li
    pivot = li.pop(0)
    small = quick_sort([i for i in li if i < pivot])
    big = quick_sort([i for i in li if i >= pivot])
    return small + [pivot] + big

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    li = list(map(int, input().split()))
    li = quick_sort(li)
    print('#{} {}'.format(tc, li[N//2]))