N, M = map(int, input().split())
li = [int(input()) for _ in range(N)]
start = 0
end = max(li) * M
ans = end
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in li:
        cnt += mid // i
    if cnt < M:
        start = mid + 1
    else:
        if ans > mid:
            ans = mid
        end = mid - 1
print(ans)