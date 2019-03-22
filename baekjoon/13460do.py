dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def sol(n):
    global ans
    if n >= ans:
        return



N, M = map(int, input().split())
ans = 11
data = [list(input()) for _ in range(N)]

if ans == 11:
    ans = -1
print(ans)