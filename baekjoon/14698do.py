import heapq
N = int(input())
for _ in range(N):
    n = int(input())
    a = list(map(int, input().split()))
    heap = list()
    ans = 1
    for i in a:
        heapq.heappush(heap, i)
    while len(heap) > 1:
        temp = heapq.heappop(heap) * heapq.heappop(heap)
        ans *= temp
        heapq.heappush(heap, temp)
    print(ans%1000000007)
