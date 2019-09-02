def sol(arr):
    visited = [False] * N
    for k in range(N - 1):
        if arr[k] == arr[k + 1]:
            continue
        elif abs(arr[k] - arr[k + 1]) > 1:
            return 0
        elif arr[k] < arr[k + 1]:
            if not visited[k]:
                visited[k] = True
                if k - L + 1 >= 0:
                    for l in range(1, L):
                        if arr[k] != arr[k - l] or visited[k - l]:
                            return 0
                        else:
                            visited[k - l] = True
                else:
                    return 0
            else:
                return 0
        else:
            if not visited[k + 1]:
                visited[k + 1] = True
                if k + L < N:
                    for l in range(2, L + 1):
                        if arr[k + 1] != arr[k + l] or visited[k + l]:
                            return 0
                        else:
                            visited[k + l] = True
                else:
                    return 0
            else:
                return 0
    return 1

N, L = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in data:
    ans += sol(i)
for j in range(N):
    ans += sol([data[i][j] for i in range(N)])
print(ans)