N, Q = map(int, input().split())
checkpoint = [tuple(map(int, input().split())) for _ in range(N)]
check = [[0] * N for i in range(N)]
query = [list(map(int, input().split()))+[_] for _ in range(Q)]
query.sort(key=lambda x: x[2])


