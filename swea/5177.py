import sys
sys.stdin = open('5177.txt', 'r')
sys.stdout = open('5177_out.txt', 'w')
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    input_li = list(map(int, input().split()))
    heap = []
    i = 0
    ans = 0
    while i < N:
        heap.append(input_li[i])
        j = i
        while j > 0:
            if heap[(j - 1) // 2] > heap[j]:
                heap[(j - 1) // 2], heap[j] = heap[j], heap[(j - 1) // 2]
            j = (j - 1) // 2
        i += 1
    i -= 1
    print(heap)
    while i > 0:
        ans += heap[(i - 1) // 2]
        i = (i - 1) // 2
    print('#{} {}'.format(test_case, ans))
