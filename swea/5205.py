# 첫번째로 하면 정렬된 경우가 있어서 런타임에러
# 가운데로 집으면 시간 초과
# 그냥 sort 썼다...
def quick_sort(li):
    if len(li) <= 1:
        return li
    pivot = li.pop(len(li)//2)
    small = quick_sort([i for i in li if i <= pivot])
    big = quick_sort([i for i in li if i > pivot])
    return small + [pivot] + big

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    li = list(map(int, input().split()))
    li = quick_sort(li)
    print('#{} {}'.format(tc, li[N//2]))