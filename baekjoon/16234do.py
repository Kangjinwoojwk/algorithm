dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
N, L, R = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
ans = 0
visit = [[True] * N for _ in range(N)]
