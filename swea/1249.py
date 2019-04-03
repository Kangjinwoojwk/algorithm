import sys
sys.stdin = open('1249.txt', 'r')
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for tc in range(1, int(input()) + 1):
    N = int(input())
    data = [list(map(int, list(input()))) for _ in range(N)]
    value = [[1 << 30] * N for _ in range(N)]
    pq = list()
    pq.append((data[0][0], 0, 0))
    while value[N - 1][N - 1] == 1 << 30:
        w, x, y = pq.pop(pq.index(min(pq))) # 리스트를 우선순위 큐처럼 쓰기 위한 조치
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if w + data[nx][ny] < value[nx][ny]: # 여기서 작은걸 확인안하고 넣기 시작하면 너무 많은 선택지가 있다
                    value[nx][ny] = w + data[nx][ny]
                    pq.append((w + data[nx][ny], nx, ny))
    print('#{} {}'.format(tc, value[N - 1][N - 1]))


# 우선 순위 큐 적용해서 줄여 보기
# from queue import PriorityQueue
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     data = [list(map(int, list(input()))) for _ in range(N)]
#     visit = [[True] * N for _ in range(N)]
#     value = [[1 << 30] * N for _ in range(N)]
#     pq = PriorityQueue()
#     pq.put((data[0][0], 0, 0))
#     while visit[N - 1][N - 1]:
#         w, x, y = pq.get()
#         for i in range(4):
#             nx, ny = x + dx[i], y + dy[i]
#             if 0 <= nx < N and 0 <= ny < N:
#                 if w + data[nx][ny] < value[nx][ny]:
#                     visit[nx][ny] = False
#                     value[nx][ny] = w + data[nx][ny]
#                     pq.put((w + data[nx][ny], nx, ny))
#     print('#{} {}'.format(tc, value[N - 1][N - 1]))

# 시간 초과
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     data = [list(map(int, list(input()))) for _ in range(N)]
#     visit = [[True] * N for _ in range(N)]
#     value = [[1 << 30] * N for _ in range(N)]
#     pq = list()
#     pq.append((data[0][0], 0, 0))
#     while visit[N - 1][N - 1]:
#         w, x, y = pq.pop(pq.index(min(pq)))
#         visit[x][y] = False
#         if value[x][y] > w:
#             value[x][y] = w
#         for i in range(4):
#             nx, ny = x + dx[i], y + dy[i]
#             if 0 <= nx < N and 0 <= ny < N:
#                 if visit[nx][ny]:
#                     pq.append((w + data[nx][ny], nx, ny))
#     print('#{} {}'.format(tc, value[N - 1][N - 1]))